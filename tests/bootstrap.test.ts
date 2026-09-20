import test from "node:test";
import assert from "node:assert/strict";
import { createServer, defaultConfig } from "../src/index.ts";

test("Bootstrap Server Test Suite", async (t) => {
  const server = createServer();

  await t.test("defaultConfig should have valid baseline properties", () => {
    assert.strictEqual(typeof defaultConfig.port, "number");
    assert.strictEqual(typeof defaultConfig.serviceName, "string");
    assert.strictEqual(typeof defaultConfig.version, "string");
    assert.ok(defaultConfig.port > 0);
  });

  await t.test("server instance should be created properly", () => {
    assert.ok(server !== null);
    assert.strictEqual(typeof server.listen, "function");
    assert.strictEqual(typeof server.close, "function");
  });
});
