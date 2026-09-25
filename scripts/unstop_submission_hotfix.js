/**
 * Unstop Platform Browser Submission Hotfix
 * 
 * Target URL: https://unstop.com/competitions/1743604/round/1593683/play/code
 * Problem:
 *   1. Windows OS defaults to empty MIME type (file_type: "") for .tsv files.
 *      Unstop's AWS S3 pre-signed URL generator rejects empty Content-Type with "Bad Request".
 *   2. On 0 previous submissions, Unstop's Angular component calls getLastSource() on
 *      null userSubmissions, throwing "TypeError: Cannot read properties of null (reading 'filter')".
 *   3. Missing error handlers cause the UI modal to hang indefinitely on "Please Wait: 0".
 * 
 * Solution:
 *   Paste this entire script into Chrome/Edge DevTools Console (F12) on the submission page.
 */

// 1. Dismiss any stuck "Please Wait" modal
document.querySelectorAll('.upload-files-bg, [class*="upload-files"]').forEach(e => e.remove());

// 2. Patch Blob and File prototypes so Windows sends verified MIME type for .tsv and .zip
Object.defineProperty(Blob.prototype, 'type', {
  get() {
    if (this.name && (this.name.endsWith('.tsv') || this.name.endsWith('.tab'))) return 'text/tab-separated-values';
    if (this.name && this.name.endsWith('.zip')) return 'application/zip';
    if (this.name && this.name.endsWith('.csv')) return 'text/csv';
    return 'text/tab-separated-values';
  },
  configurable: true
});

Object.defineProperty(File.prototype, 'type', {
  get() {
    if (this.name && (this.name.endsWith('.tsv') || this.name.endsWith('.tab'))) return 'text/tab-separated-values';
    if (this.name && this.name.endsWith('.zip')) return 'application/zip';
    if (this.name && this.name.endsWith('.csv')) return 'text/csv';
    return 'text/tab-separated-values';
  },
  configurable: true
});

// 3. Patch Object.prototype.userSubmissions to prevent Angular null.filter crash
Object.defineProperty(Object.prototype, 'userSubmissions', {
  get() { return this._us || []; },
  set(v) { this._us = (v === null || v === undefined) ? [] : v; },
  configurable: true
});

// 4. Re-enable Submit & Evaluate button
document.querySelectorAll('button').forEach(b => {
  if (b.innerText && b.innerText.includes('Submit')) {
    b.disabled = false;
    b.removeAttribute('disabled');
  }
});

console.log("%c[SUCCESS] Unstop Submission Hotfix Applied! Click 'Submit & Evaluate' now.", "color: #10b981; font-weight: bold; font-size: 14px;");
