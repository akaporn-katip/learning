'use strict';

const apiGateway = require('..');
const assert = require('assert').strict;

assert.strictEqual(apiGateway(), 'Hello from apiGateway');
console.info('apiGateway tests passed');
