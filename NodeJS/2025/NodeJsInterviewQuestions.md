## NodeJS Interview Questions


### 1. What is the difference between spawn and exec in child_process?
- **spawn**: Launches a new process with a given command, streaming data via stdin/stdout/stderr. Suitable for long-running processes (e.g., streaming logs). Returns a `ChildProcess` object.
- **exec**: Runs a command in a shell and buffers the output, returning it in a callback. Best for short-lived commands (e.g., `ls`). Less efficient for large outputs due to buffering.

---

### 2. How do you debug Node.js applications?
- **Built-in Debugger**: Use `node inspect` or `--inspect` flag with Chrome DevTools (`chrome://inspect`).
- **VS Code**: Configure `launch.json` for breakpoints and step-through debugging.
- **Logging**: Use `console.log` or libraries like `debug`.
- **Tools**: Use `ndb`, `node-inspector`, or profiling tools like `clinic.js`.

---

### 3. What is the role of body-parser or express.json?
- **body-parser**: Middleware to parse incoming request bodies (e.g., JSON, URL-encoded) into `req.body`. Deprecated in favor of Express’s built-in parsers.
- **express.json**: Built-in Express middleware (since Express 4.16.0) to parse JSON payloads into `req.body`. Example: `app.use(express.json())`.

---

### 4. How do you store passwords securely in Node.js?
Use `bcrypt` or `argon2` to hash passwords:
- Generate a salt and hash the password.
- Store the hash in the database.
- Compare hashes during login.
Example: `bcrypt.hash(password, 10)` and `bcrypt.compare(password, hash)`.

---

### 5. How do you manage error handling in Express?
- **Middleware**: Use error-handling middleware with four parameters: `(err, req, res, next)`.
- **Try-Catch**: Wrap async code in try-catch blocks.
- **Centralized Handling**: Define a global error handler at the end of middleware stack.
Example:
```javascript
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});
```

---

### 6. How do you handle transactions in Node.js?
- **SQL Databases**: Use libraries like `knex` or `Sequelize` with transaction support. Example: `knex.transaction(trx => {...})`.
- **MongoDB**: Use `session.startTransaction()` and `session.commitTransaction()` (MongoDB 4.0+).
- Ensure rollback on errors using `try-catch`.

---

### 7. What is Mocha/Chai and how are they used in testing?
- **Mocha**: A test framework for running and organizing tests (describe, it blocks).
- **Chai**: An assertion library for writing test expectations (expect, should, assert).
- Usage: Write tests in Mocha, use Chai for assertions. Example:
```javascript
const chai = require('chai');
const expect = chai.expect;
describe('Math', () => {
  it('adds numbers', () => {
    expect(1 + 1).to.equal(2);
  });
});
```

---

### 8. How do you store session data securely?
- Use `express-session` with a secure store (e.g., `connect-redis`, `connect-mongo`).
- Enable `secure: true` for HTTPS cookies.
- Set `httpOnly` and `sameSite` to prevent XSS.
- Encrypt session data and use a strong secret.

---

### 9. What is the difference between asynchronous and non-blocking?
- **Asynchronous**: Operations that execute independently, with results handled later (e.g., via callbacks, promises).
- **Non-blocking**: Operations that don’t halt the event loop, allowing other tasks to proceed. Node.js is non-blocking, enabling async operations like I/O.

---

### 10. What is Helmet and how does it help with security?
- **Helmet**: A collection of middleware to set security-related HTTP headers.
- Helps with: XSS protection (`X-XSS-Protection`), preventing clickjacking (`X-Frame-Options`), disabling MIME sniffing, and more.
- Example: `app.use(helmet())`.

---

### 11. How do you implement user authentication in Node.js?
- Use `passport` or custom logic with JWT/`bcrypt`.
- Steps: Register user (hash password), login (verify credentials, issue token), protect routes (verify token).
- Example: Use `jsonwebtoken` for JWT and `express-jwt` for route protection.

---

### 12. What is the difference between console.log and util.debuglog?
- **console.log**: Outputs to stdout/stderr, always visible.
- **util.debuglog**: Outputs debug messages only if `NODE_DEBUG` env variable matches the section name. Example: `const debug = util.debuglog('myapp'); debug('Message');`.

---

### 13. How does async/await work in Node.js?
- **async**: Marks a function as asynchronous, returning a Promise.
- **await**: Pauses execution until a Promise resolves, used inside async functions.
- Example:
```javascript
async function fetchData() {
  const data = await someAsyncCall();
  return data;
}
```

---

### 14. How do you handle high concurrency in Node.js?
- Use the **cluster** module to utilize multiple CPU cores.
- Implement load balancing with `pm2` or external tools like Nginx.
- Use async I/O to avoid blocking the event loop.
- Optimize database queries and caching (e.g., Redis).

---

### 15. What are some tips to improve performance in Node.js?
- Use async operations to avoid blocking.
- Implement caching (e.g., Redis).
- Optimize database queries (indexing, batching).
- Use clustering for multi-core usage.
- Profile with tools like `clinic.js` or `--prof`.
- Minimize middleware overhead.

---

### 16. What is Node.js and how does it work?
- **Node.js**: A runtime for executing JavaScript outside the browser, built on Chrome’s V8 engine.
- **How it works**: Uses an event-driven, non-blocking I/O model with a single-threaded event loop, handling async operations via callbacks, promises, or async/await.

---

### 17. What is rate limiting and why is it important?
- **Rate limiting**: Restricts the number of requests a client can make in a time window.
- **Importance**: Prevents abuse, protects server resources, ensures fair usage, and mitigates DDoS attacks.
- Example: Use `express-rate-limit`.

---

### 18. Explain the concept of callbacks in Node.js.
- **Callbacks**: Functions passed as arguments to execute after an async operation completes.
- Example:
```javascript
fs.readFile('file.txt', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```
- Issue: Can lead to callback hell; mitigated by Promises or async/await.

---

### 19. Implement a rate limiter middleware in Node.js

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per window
  message: 'Too many requests, please try again later.',
});

module.exports = limiter;

// Usage in Express app:
// const express = require('express');
// const app = express();
// app.use(limiter);
```

---

### 20. What are popular testing libraries for Node.js?
- **Mocha**: Test framework for structure.
- **Chai**: Assertion library.
- **Jest**: All-in-one testing framework with mocking.
- **Supertest**: For HTTP API testing.
- **Sinon**: For spies, stubs, and mocks.

---

### 21. How do you handle command-line arguments in Node.js?
- Use `process.argv` (array of arguments, starting with node path and script name).
- Example: `node script.js arg1` → `process.argv[2] = 'arg1'`.
- Use libraries like `yargs` or `commander` for advanced parsing.

---

### 22. How do you write unit tests for a Node.js module?
- Use Mocha/Chai or Jest.
- Export the module’s functions.
- Write test cases with assertions.
Example:
```javascript
// math.js
exports.add = (a, b) => a + b;

// math.test.js
const { expect } = require('chai');
const { add } = require('./math');
describe('Math', () => {
  it('should add two numbers', () => {
    expect(add(2, 3)).to.equal(5);
  });
});
```

---

### 23. What are CommonJS and ES Modules?
- **CommonJS**: Node’s default module system using `require` and `module.exports`. Synchronous loading.
- **ES Modules**: Standard JavaScript modules using `import`/`export`. Supports async loading, used with `"type": "module"` in `package.json`.

---

### 24. What is the difference between synchronous and asynchronous file operations?
- **Synchronous**: Blocks the event loop until complete (e.g., `fs.readFileSync`).
- **Asynchronous**: Non-blocking, uses callbacks/promises (e.g., `fs.readFile`).
- Async is preferred for performance in I/O-heavy apps.

---

### 25. How do you connect Node.js to PostgreSQL or MySQL?
- **PostgreSQL**: Use `pg` or `knex`. Example: `const { Pool } = require('pg'); const pool = new Pool({ user: 'me', database: 'mydb' });`.
- **MySQL**: Use `mysql2` or `knex`. Example: `const mysql = require('mysql2'); const connection = mysql.createConnection({ host: 'localhost', user: 'me' });`.
- Use connection pools for scalability.

---

### 26. What is Passport.js and how is it used?
- **Passport.js**: Authentication middleware for Node.js.
- **Usage**: Supports strategies (e.g., local, OAuth, JWT). Configure with `passport.use`, authenticate with `passport.authenticate`.
- Example: Local strategy for username/password login.

---

### 27. How do you handle routing in Express?
- Define routes using `app.get`, `app.post`, etc., or use `express.Router` for modular routing.
- Example:
```javascript
const router = express.Router();
router.get('/users', (req, res) => res.json(users));
app.use('/api', router);
```

---

### 28. How do you create a REST API using Express?

```javascript
const express = require('express');
const app = express();
app.use(express.json());

let users = [{ id: 1, name: 'Alice' }];

app.get('/users', (req, res) => res.json(users));
app.post('/users', (req, res) => {
  const user = req.body;
  users.push(user);
  res.status(201).json(user);
});
app.get('/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json(user);
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

---

### 29. How can you spawn child processes in Node.js?
- Use `child_process` module’s `spawn`, `exec`, `execFile`, or `fork`.
- Example with `spawn`:
```javascript
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh']);
ls.stdout.on('data', data => console.log(data.toString()));
```

---

### 30. What are Promises in Node.js?
- **Promises**: Objects representing the eventual completion (or failure) of an async operation.
- States: Pending, Fulfilled, Rejected.
- Example:
```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Done'), 1000);
});
promise.then(result => console.log(result));
```

---

### 31. How would you implement pagination in an API?
- Use query parameters (e.g., `page`, `limit`).
- Calculate offset: `offset = (page - 1) * limit`.
- Example:
```javascript
app.get('/items', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const offset = (page - 1) * limit;
  const paginatedItems = items.slice(offset, offset + limit);
  res.json(paginatedItems);
});
```

---

### 32. What is package.json?
- **package.json**: A metadata file for Node.js projects, defining the project’s name, version, dependencies, scripts, and more.
- Example:
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "dependencies": { "express": "^4.17.1" }
}
```

---

### 33. What is the difference between devDependencies and dependencies?
- **dependencies**: Packages required for production (e.g., `express`).
- **devDependencies**: Packages for development/testing (e.g., `mocha`, `nodemon`).
- Installed with `npm install --save` vs. `--save-dev`.

---

### 34. How does Node.js handle concurrency?
- Uses a single-threaded event loop with non-blocking I/O.
- Async operations (e.g., file reads, HTTP requests) are offloaded to the libuv thread pool.
- Clustering or worker threads can utilize multiple cores.

---

### 35. What is the purpose of the 'require' function?
- **require**: Imports modules in CommonJS, resolving and loading them synchronously.
- Example: `const fs = require('fs');`.

---

### 36. How do you connect Node.js to MongoDB?
- Use `mongoose` or `mongodb` driver.
- Example with `mongoose`:
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/mydb', { useNewUrlParser: true });
```

---

### 37. How does Node.js resolve modules?
- **Resolution**: Checks `node_modules` (local, then parent directories), core modules, or paths specified in `NODE_PATH`.
- Order: Core modules > file paths > `node_modules`.

---

### 38. Build a GraphQL API using Node.js

```javascript
const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');

const schema = buildSchema(`
  type Query {
    hello: String
    user(id: Int!): User
  }
  type User {
    id: Int
    name: String
  }
`);

const root = {
  hello: () => 'Hello, GraphQL!',
  user: ({ id }) => ({ id, name: `User${id}` }),
};

const app = express();
app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true,
}));
app.listen(3000, () => console.log('GraphQL server on port 3000'));
```

---

### 39. How do you handle large file uploads efficiently?
- Use streams with `multer` for Express.
- Process files in chunks to avoid memory overload.
- Example: `multer({ storage: multer.diskStorage({...}) })`.

---

### 40. How would you schedule cron jobs in Node.js?
- Use `node-cron` or `node-schedule`.
- Example with `node-cron`:
```javascript
const cron = require('node-cron');
cron.schedule('0 0 * * *', () => console.log('Daily task'));
```

---

### 41. What is CORS and how do you enable it?
- **CORS**: Cross-Origin Resource Sharing, controls cross-domain requests.
- Enable in Express: `app.use(cors())` (from `cors` package).
- Example:
```javascript
const cors = require('cors');
app.use(cors({ origin: 'http://example.com' }));
```

---

### 42. What are the key features of Node.js?
- Asynchronous, non-blocking I/O.
- Event-driven architecture.
- Built on V8 engine for fast JavaScript execution.
- Single-threaded with event loop.
- Extensive module ecosystem via npm.

---

### 43. How do you prevent memory leaks in a Node.js application?
- Avoid global variables that grow indefinitely.
- Use streams for large data.
- Monitor with `heapdump` or `--inspect`.
- Clean up event listeners.
- Profile with `clinic.js`.

---

### 44. Create a CLI tool using Node.js

```javascript
#!/usr/bin/env node
const yargs = require('yargs');

yargs.command({
  command: 'greet <name>',
  describe: 'Greet a user',
  handler(argv) {
    console.log(`Hello, ${argv.name}!`);
  },
}).demandCommand().help().argv;
```

---

### 45. How do you implement file uploads in Express?
- Use `multer` middleware.
- Example:
```javascript
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });
app.post('/upload', upload.single('file'), (req, res) => {
  res.send('File uploaded');
});
```

---

### 46. How do you handle errors in async code?
- Use try-catch with async/await.
- Example:
```javascript
app.get('/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (err) {
    next(err);
  }
});
```

---

### 47. What is Sequelize ORM?
- **Sequelize**: An ORM for SQL databases (MySQL, PostgreSQL, etc.).
- Features: Model definitions, associations, migrations, query building.
- Example: Define a model with `Sequelize.define`.

---

### 48. How do you profile a Node.js application?
- Use `--prof` flag for V8 profiling.
- Analyze with `node --prof-process`.
- Use `clinic.js` for CPU/memory profiling.
- Example: `node --prof app.js`.

---

### 49. Design a RESTful API for a Todo app

```javascript
const express = require('express');
const app = express();
app.use(express.json());

let todos = [];
let id = 1;

app.get('/todos', (req, res) => res.json(todos));
app.post('/todos', (req, res) => {
  const todo = { id: id++, title: req.body.title, done: false };
  todos.push(todo);
  res.status(201).json(todo);
});
app.put('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todo = todos.find(t => t.id === id);
  if (!todo) return res.status(404).json({ error: 'Not found' });
  todo.title = req.body.title || todo.title;
  todo.done = req.body.done !== undefined ? req.body.done : todo.done;
  res.json(todo);
});
app.delete('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  todos = todos.filter(t => t.id !== id);
  res.status(204).send();
});

app.listen(3000, () => console.log('Todo API on port 3000'));
```

---

### 50. How do you create and publish a package on npm?
- Create a module with `package.json` (`npm init`).
- Write code in `index.js`.
- Login to npm: `npm login`.
- Publish: `npm publish`.
- Ensure unique package name and proper versioning.

---

### 51. Explain the Node.js event loop.
- **Event Loop**: Manages async operations in a single-threaded environment.
- Phases: Timers, Pending Callbacks, Idle/Prepare, Poll, Check, Close Callbacks.
- Handles callbacks, I/O, and timers without blocking.

---

### 52. Design a real-time notification system
- Use **Socket.IO** or **WebSocket**.
- Steps: Set up a WebSocket server, broadcast notifications to connected clients.
- Example: Use `socket.io` with Express for real-time updates.

---

### 53. How do you implement role-based access control?
- Define roles (e.g., admin, user) in user model.
- Use middleware to check roles.
- Example:
```javascript
const restrictTo = (...roles) => (req, res, next) => {
  if (!roles.includes(req.user.role)) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  next();
};
app.get('/admin', restrictTo('admin'), (req, res) => res.json({}));
```

---

### 54. What is npm?
- **npm**: Node Package Manager, a tool for managing dependencies and publishing packages.
- Commands: `npm install`, `npm publish`, `npm run`.

---

### 55. What is callback hell and how do you avoid it?
- **Callback Hell**: Nested callbacks making code hard to read.
- Avoid with:
  - Promises: Chain with `.then`.
  - Async/await: Cleaner syntax.
  - Modularize code into functions.

---

### 56. What is the difference between Node.js and JavaScript in the browser?
- **Node.js**: Server-side runtime with access to file system, OS, and network APIs.
- **Browser JS**: Runs in a browser, accesses DOM, `window`, and browser APIs.
- Node.js uses CommonJS/ES Modules; browsers use ES Modules.

---

### 57. How do you work with streams in Node.js?
- **Streams**: Handle data in chunks for efficient I/O.
- Types: Readable, Writable, Duplex, Transform.
- Example:
```javascript
const fs = require('fs');
fs.createReadStream('input.txt').pipe(fs.createWriteStream('output.txt'));
```

---

### 58. How do you protect against SQL Injection and XSS in Node.js?
- **SQL Injection**: Use parameterized queries (e.g., `knex`, `pg`).
- **XSS**: Sanitize inputs with `sanitize-html`, set `X-XSS-Protection` header via Helmet.
- Example: Use `express-validator` for input validation.

---

### 59. What are middleware functions in Express?
- Functions that process requests/responses in the request-response cycle.
- Types: Application-level, router-level, error-handling.
- Example: `app.use(express.json())`.

---

### 60. What are common security issues in Node.js applications?
- **SQL Injection**: Mitigate with parameterized queries.
- **XSS**: Sanitize inputs.
- **CSRF**: Use `csurf` middleware.
- **Insecure Dependencies**: Audit with `npm audit`.
- **Uncaught Exceptions**: Handle with `process.on('uncaughtException')`.

---

### 61. How do you read/write files in Node.js?
- Use `fs` module.
- Example:
```javascript
const fs = require('fs');
fs.writeFileSync('file.txt', 'Hello');
fs.readFile('file.txt', 'utf8', (err, data) => console.log(data));
```

---

### 62. What are JWTs and how are they used in authentication?
- **JWT**: JSON Web Tokens, compact tokens for authentication (header, payload, signature).
- Usage: Issue token on login, verify on protected routes.
- Example: Use `jsonwebtoken` to sign/verify tokens.

---

### 63. What is Jest and how is it different from Mocha?
- **Jest**: Testing framework with built-in assertions, mocking, and coverage.
- **Mocha**: Flexible framework, requires external assertion libraries (e.g., Chai).
- Jest is easier to set up; Mocha is more customizable.

---

### 64. What are the global objects in Node.js?
- `global`: Node’s global namespace (like `window` in browsers).
- Others: `process`, `console`, `Buffer`, `__dirname`, `__filename`.

---

### 65. How does load balancing work in Node.js applications?
- Distribute traffic across multiple Node.js instances.
- Tools: Nginx, AWS ELB, or Node’s `cluster` module.
- Example: Use `pm2` to run multiple processes.

---

### 66. How do you manage memory usage in Node.js?
- Avoid memory leaks (e.g., unclosed streams, global vars).
- Use streams for large data.
- Monitor with `heapdump` or `--inspect`.
- Limit buffer sizes in streams.

---

### 67. What is Express.js?
- **Express.js**: A minimal web framework for Node.js, simplifying HTTP server creation, routing, and middleware.
- Example: `const app = require('express')()`.

---

### 68. What is the role of V8 in Node.js?
- **V8**: Google’s JavaScript engine, compiles and executes JavaScript in Node.js.
- Provides high performance and JIT compilation.

---

### 69. How would you build a scalable chat application?
- Use **Socket.IO** for real-time communication.
- Store messages in a database (e.g., MongoDB).
- Scale with Redis for pub/sub and clustering.
- Deploy with load balancer (e.g., Nginx).

---

### 70. How do you validate incoming data in a request?
- Use `express-validator` or `joi`.
- Example with `express-validator`:
```javascript
const { body, validationResult } = require('express-validator');
app.post('/user', [
  body('email').isEmail(),
  body('password').isLength({ min: 6 }),
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) return res.status(400).json(errors.array());
  res.json(req.body);
});
```

---

### 71. What is the difference between process.nextTick() and setImmediate()?
- **process.nextTick()**: Executes before the next event loop tick, higher priority.
- **setImmediate()**: Executes after I/O callbacks in the current tick.
- Use `nextTick` for critical tasks, `setImmediate` for deferring non-critical ones.

---

### 72. Build a file upload endpoint in Node.js

<xaiArtifact artifact_id="d8f6c7a9-4e2c-4 DIY://buildFileUploadEndpoint.js
const express = require('express');
const multer = require('multer');
const app = express();
const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }
  res.json({ message: 'File uploaded', file: req.file });
});

app.listen(3000, () => console.log('Server on port 3000'));
</xaiArtifact>

---

### 73. What is mocking and how do you use it in tests?
- **Mocking**: Replacing real dependencies with fake implementations for testing.
- Use `sinon` or Jest’s mocking.
- Example with `sinon`:
```javascript
const sinon = require('sinon');
const db = require('./db');
sinon.stub(db, 'query').returns(Promise.resolve([]));
```

---

### 74. What is the difference between require and import?
- **require**: CommonJS, synchronous, used in Node.js.
- **import**: ES Modules, supports async, used with `"type": "module"`.
- Example: `const fs = require('fs')` vs. `import fs from 'fs'`.

---

### 75. Implement a logging system using Winston

```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
    new winston.transports.Console(),
  ],
});

logger.info('Application started');
logger.error('Something went wrong');
```

---

### 76. What is Mongoose and how is it used?
- **Mongoose**: An ODM (Object Data Modeling) library for MongoDB.
- Usage: Define schemas, models, and perform CRUD operations.
- Example:
```javascript
const mongoose = require('mongoose');
const User = mongoose.model('User', new mongoose.Schema({ name: String }));
```

---

### 77. What are clusters in Node.js?
- **Clusters**: Allow Node.js to fork multiple processes to utilize CPU cores.
- Example:
```javascript
const cluster = require('cluster');
if (cluster.isMaster) {
  for (let i = 0; i < require('os').cpus().length; i++) {
    cluster.fork();
  }
} else {
  require('./app');
}
```

---

### Notes
- **Running Code**: Ensure Node.js is installed. Install dependencies (e.g., `express`, `multer`, `winston`) with `npm install <package>`. Run scripts with `node filename.js`.
- **Testing APIs**: Use `curl` or Postman for REST/GraphQL APIs (e.g., problems 28, 38, 49, 72).
- **PDF Request**: If you want a PDF, I can consolidate answers into a Markdown or LaTeX file for conversion (similar to previous responses). Please confirm your preference.
- **Further Details**: If you need deeper explanations, additional test cases, or specific questions expanded, let me know!
