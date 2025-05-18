### React.js Interview Questions (150)

#### ✨ Fundamentals

**1. What is React and why is it used?**
A JavaScript library for building UIs. It uses a component model and virtual DOM to efficiently render and update views, making development of interactive, stateful apps easier.

**2. What are the main features of React?**

* **JSX**: HTML-like syntax in JavaScript
* **Components**: Reusable, composable UI building blocks
* **Virtual DOM**: Fast diff-and-patch rendering
* **Unidirectional data flow**: Predictable state management
* **Hooks**: Simplify state and side-effects in function components

**3. What is JSX?**
A syntax extension that lets you write XML-like tags in JavaScript. Under the hood it compiles to `React.createElement` calls, producing element objects.

**4. How does the virtual DOM work?**
React maintains an in-memory tree of elements. On state/prop changes it diffs the new tree against the previous, then batches minimal real DOM updates for performance.

**5. What are components in React?**
Self-contained units that manage their own structure, style, and behavior. They can be function or class-based, and can compose other components.

**6. What is the difference between functional and class components?**

* **Functional**: Plain functions; use Hooks for state and lifecycles; simpler and preferred.
* **Class**: ES6 classes; have `this.state` and lifecycle methods (`componentDidMount`, etc.); more verbose.

**7. What is the difference between state and props?**

* **State**: Internal, mutable data in a component (`useState` or `this.state`).
* **Props**: External, read-only inputs passed from parent to child.

**8. What are controlled and uncontrolled components?**

* **Controlled**: Form inputs whose value is driven by React state (via `value` and `onChange`).
* **Uncontrolled**: Inputs that maintain their own internal DOM state, accessed via refs.

**9. What are keys in React and why are they important?**
Unique identifiers for items in a list. They help React match elements between renders to preserve state and minimize re-renders.

**10. How do you conditionally render components in React?**
Use JavaScript conditionals in JSX:

```jsx
{isLoggedIn
  ? <Dashboard />
  : <LoginForm />}
```

Or logical operators:

```jsx
{items.length && <ItemList items={items} />}
```

---

#### ⚖️ State & Props

**11. How do you update the state in React?**

* **Function components**: Call the setter from `useState` (e.g., `setCount(count + 1)`).
* **Class components**: Call `this.setState({ key: value })` (merges state).

**12. What is the role of the setState function?**
Schedules a state update and re-run of the component. In classes it merges state; in Hooks, it replaces the state value.

**13. What happens when state changes in React?**
React re-invokes the component function (or runs `render()` in classes), diffs the virtual DOM, and applies minimal updates to the real DOM.

**14. How do you pass data between components?**

* **Parent → Child**: Via props (`<Child data={value} />`).
* **Child → Parent**: Pass a callback prop (`onChange={handleChange}`) that the child calls.
* **Across tree**: Use Context or state-management libraries.

**15. What are default props?**
Fallback values for props if nothing is passed. Defined via `Component.defaultProps = { … }` or default parameters in function signatures.

**16. What are propTypes?**
Runtime type-checking for props in development. Defined via `Component.propTypes = { name: PropTypes.string.isRequired, … }`.

**17. What is prop drilling and how can you avoid it?**
Passing props through many intermediate components. Avoid by using React Context, Redux/MobX, or custom hooks for shared state.

**18. How do you share state between components?**

* Lift state up to the nearest common ancestor.
* Use React Context for global or cross-tree state.
* Employ external stores (Redux, Zustand, Recoil).

**19. How do you handle form state in React?**

* **Controlled**: Manage each input’s `value` and `onChange` in state.
* **Uncontrolled**: Use refs with `defaultValue` and read values on submit.
* Use form libraries (Formik, React Hook Form) for complex forms.

**20. How do you lift state up in a component tree?**
Move the shared state into the closest common parent, pass it down as props to children, and pass callbacks to modify it back up from child components.


---

#### 🎓 Hooks

**21. What are React Hooks?**
Functions that let you “hook into” React state and lifecycle features from function components without writing classes.

**22. What is the use of useState?**
Declares state in a function component. Returns a state value and a setter function to update it, triggering re-renders.

**23. How does useEffect work?**
Runs side-effects after render. By default, after every render; with a dependency array, only when specified values change; and with an empty array, only once on mount.

**24. What is useContext and how is it used?**
Consumes a React Context in a function component. Call `const value = useContext(MyContext)` to read the nearest provider’s value and subscribe to its updates.

**25. What is useRef and how do you use it?**
Returns a mutable ref object (`.current`) that persists across renders. Use it to reference DOM nodes or store mutable values without causing re-renders.

**26. How does useMemo optimize performance?**
Memoizes a computed value: `useMemo(() => computeExpensive(a, b), [a, b])`. Re-computes only when dependencies change, avoiding expensive recalculations on every render.

**27. What is useCallback used for?**
Memoizes a callback function: `useCallback(fn, [deps])`. Returns the same function instance between renders unless dependencies change—useful to prevent unnecessary child re-renders or effect re-runs.

**28. What are custom hooks?**
Reusable functions that call built-in hooks to encapsulate and share stateful logic (e.g., `useFetch`, `useForm`). They start with the `use` prefix.

**29. What are the rules of hooks?**

1. Call hooks only at the top level of React functions (no loops or conditionals).
2. Call hooks only from React function components or custom hooks.
3. Always use the same hook call order on every render.

**30. Can you use hooks in class components?**
No. Hooks work only in function components (or other custom hooks), not in class components.

---

#### 🔄 Lifecycle

**31. What are lifecycle methods in React?**
Special methods in class components that run at different phases: mounting (`constructor`, `componentDidMount`), updating (`shouldComponentUpdate`, `componentDidUpdate`), and unmounting (`componentWillUnmount`).

**32. What is componentDidMount used for?**
Runs once after the component mounts. Commonly used for fetching data, setting up subscriptions, or imperative DOM operations.

**33. What is componentDidUpdate?**
Runs after every update (re-render), receiving previous props and state. Use it to react to prop or state changes (e.g., fetch new data when inputs change).

**34. What is componentWillUnmount?**
Runs just before a component is removed. Clean up subscriptions, timers, or other resources to prevent memory leaks.

**35. How do you handle side effects in functional components?**
Use the `useEffect` hook, specifying dependencies to control when effects run, and return a cleanup function for unmount logic.

**36. How do lifecycle methods translate into hooks?**

* `componentDidMount` & `componentDidUpdate` → `useEffect(() => { /* effect */ }, [deps])`
* `componentWillUnmount` → return cleanup from `useEffect`
* `shouldComponentUpdate` → `React.memo` for pure functional components

**37. What is the useLayoutEffect hook?**
Like `useEffect` but fires synchronously after all DOM mutations and before the browser paints. Use for reading layout or triggering synchronous re-rendering.

**38. How do you avoid memory leaks in useEffect?**
Return a cleanup function from your effect that cancels timers, unsubscribes from event listeners or aborts in-flight async tasks when dependencies change or component unmounts.

**39. How do you handle API calls in lifecycle methods?**

* **Class**: Fetch in `componentDidMount`, store results in state; cancel requests in `componentWillUnmount`.
* **Function**: Fetch in `useEffect(() => { fetch...; return cancel }, [])`, storing results via `useState` and cleaning up on unmount.

**40. What is the difference between useEffect and useLayoutEffect?**

* **useEffect**: Runs asynchronously after the browser paints—won’t block UI updates.
* **useLayoutEffect**: Runs synchronously before the browser paints—blocks rendering until effect and cleanup complete, useful for DOM measurements or synchronous mutations.

---

Feel free to ask for deeper examples or code samples!


---

#### ⚖️ Routing (React Router)

**41. What is React Router?**
A library for handling client-side routing in React applications. It maps URLs to components, enabling SPA navigation without full page reloads.

**42. How do you implement routing in React?**
Wrap your app in a `<BrowserRouter>` (or `<HashRouter>`), define `<Routes>` with `<Route path="…" element={<Component/>}>`, and use `<Link>` or `<NavLink>` for navigation.

**43. What is the use of useNavigate or useHistory?**
These hooks let you imperatively navigate:

* **useNavigate** (v6): returns a function `navigate(to, options)` to push or replace history entries.
* **useHistory** (v5): gives access to `history.push`, `history.replace`, etc.

**44. How do you create nested routes in React?**
Define child `<Route>`s inside a parent `<Route>` and render an `<Outlet />` in the parent component where children should appear.

```jsx
<Routes>
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="stats" element={<Stats />} />
  </Route>
</Routes>
```

**45. What is route-based code splitting?**
Loading route components lazily with `React.lazy` and `<Suspense>` so each route’s code bundle is fetched only when that path is visited, reducing initial load size.

**46. How do you handle redirection in React Router?**

* **v6**: Use `<Navigate to="/login" replace />` in route definitions or call `navigate("/login", { replace: true })`.
* **v5**: Use `<Redirect to="/login" />` or `history.replace("/login")`.

**47. What is a catch-all route?**
A route that matches any unspecified path (often a 404 page). Defined using a wildcard:

```jsx
<Route path="*" element={<NotFound />} />
```

**48. How do you create a protected route?**
Wrap a `<Route>` or component in an auth-checking component that renders children if authenticated or redirects otherwise:

```jsx
function PrivateRoute({ children }) {
  return isAuth ? children : <Navigate to="/login" />;
}
```

**49. What is lazy loading in routing?**
Deferring the loading of route components until they’re needed by using `React.lazy(() => import('./MyPage'))` and `<Suspense>` to show a fallback while loading.

**50. How do you get query parameters in React Router?**
Use the `useLocation` hook and parse `location.search` with `URLSearchParams`:

```js
const { search } = useLocation();
const params = new URLSearchParams(search);
const id = params.get('id');
```

---

#### 💡 Context API

**51. What is the Context API?**
A React feature for sharing data (like theme or auth) across the component tree without prop drilling. It uses `createContext`, `Provider`, and `useContext`.

**52. How do you create a context in React?**

```js
const MyContext = React.createContext(defaultValue);
```

**53. How do you provide and consume context values?**

* **Provide**: Wrap components with `<MyContext.Provider value={value}>…</MyContext.Provider>`.
* **Consume**: In children, call `const value = useContext(MyContext)` or use `<MyContext.Consumer>`.

**54. What is the difference between Redux and Context API?**

* **Redux**: Full-fledged state-management library with middleware, devtools, and predictable reducers; better for complex global state.
* **Context API**: Built-in, lightweight for passing data; can lead to re-renders if overused; lacks middleware and strict patterns.

**55. How do you use useContext in a component?**

```js
import { useContext } from 'react';
const theme = useContext(ThemeContext);
```

**56. How do you avoid prop drilling using Context API?**
Place a context provider high in the tree and consume the context in deeply nested components instead of passing props through every level.

**57. How do you structure nested contexts?**
Nest `<Provider>`s so each context wraps only the components that need it:

```jsx
<AuthProvider>
  <ThemeProvider>
    <App />
  </ThemeProvider>
</AuthProvider>
```

**58. What is the role of Provider and Consumer?**

* **Provider**: Supplies a context value to all descendants.
* **Consumer**: A component or hook (`useContext`) that reads the current context value.

**59. Can context trigger unnecessary renders?**
Yes. Any change to the `value` prop of a Provider re-renders all consuming components. Mitigate by memoizing the `value` object or splitting contexts.

**60. What are some limitations of the Context API?**

* Can cause performance issues due to broad re-renders.
* Not suited for high-frequency updates (e.g., animation frames).
* Lacks middleware, time-travel debugging, and strict structure compared to state libraries like Redux.

---

Feel free to send more when you’re ready!


---

#### 🚀 Performance Optimization

**61. What is React.memo?**
A higher-order component that memoizes a functional component’s rendered output. It shallowly compares props and skips re-render if they haven’t changed.

**62. What is useMemo and when should it be used?**
A hook that memoizes the result of a computation:

```js
const expensiveValue = useMemo(() => compute(a, b), [a, b]);
```

Use it to avoid re-running expensive calculations on every render when dependencies are unchanged.

**63. What is the difference between useMemo and useCallback?**

* **useMemo** returns a memoized value.
* **useCallback** returns a memoized function reference.
  Internally, `useCallback(fn, deps)` is shorthand for `useMemo(() => fn, deps)`.

**64. How do you prevent unnecessary renders?**

* Memoize components with `React.memo`.
* Memoize callbacks/values with `useCallback`/`useMemo`.
* Split context to minimize consumers.
* In class components, implement `shouldComponentUpdate` or extend `PureComponent`.

**65. What is lazy loading and how is it implemented?**
Deferring component loading until needed using `React.lazy()` and `<Suspense>`:

```js
const LazyComp = React.lazy(() => import('./Comp'));
<Suspense fallback={<Spinner />}><LazyComp /></Suspense>
```

**66. How does React handle reconciliation?**
React builds a new virtual DOM on each render, diffs it against the previous tree using its fiber algorithm, and applies the minimal set of DOM mutations to sync them.

**67. What is the role of shouldComponentUpdate?**
A class lifecycle method that lets you compare next props/state with current ones and return `false` to skip re-render. It’s a manual optimization akin to `React.PureComponent`.

**68. How does key prop affect performance?**
Keys help React identify which items in a list have changed, moved, or been removed. Stable keys minimize reordering work and preserve component state, speeding up list diffing.

**69. How do you monitor React performance?**

* Use **React DevTools Profiler** to record renders and flamegraphs.
* Measure real-world metrics (FPS, TTI) with **Web Vitals** or **Lighthouse**.
* Instrument with custom timers or performance marks.

**70. What are the best practices for optimizing large React apps?**

* Code-split routes and heavy components.
* Use memoization (`React.memo`, `useMemo`, `useCallback`) judiciously.
* Virtualize long lists (e.g., react-window).
* Keep component trees shallow and props minimal.
* Lazy-load images and assets.
* Analyze bundle size and remove unused code (tree-shaking).

---

#### 📅 Forms & Events

**71. How do you handle form submission in React?**
Attach an `onSubmit` handler to the `<form>` element, call `event.preventDefault()`, and process form data from state or refs.

```jsx
function onSubmit(e) {
  e.preventDefault();
  // handle form data
}
```

**72. What is the use of event.preventDefault()?**
Stops the browser’s default behavior (e.g., page reload on form submit or link navigation) so you can handle the event in JavaScript.

**73. How do you manage multiple form inputs?**

* **Controlled**: Keep each input value in state, update via a generic `onChange` handler using the input’s `name` attribute.

  ```js
  const [form, setForm] = useState({ username: '', email: '' });
  function onChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }
  ```
* **Uncontrolled**: Use refs to read values on submit.

**74. How do you validate form inputs in React?**

* Inline in `onChange`/`onBlur` handlers, setting error state.
* Use HTML5 validation attributes (`required`, `pattern`).
* Employ libraries like **Yup** with **Formik** or **React Hook Form** for schema-based validation.

**75. What is Formik and how does it help?**
A form library that abstracts form state management, validation, and submission. It provides hooks/components (`useFormik`, `<Field>`, `<Form>`) to reduce boilerplate.

**76. What are controlled components?**
Inputs whose value and updates are fully driven by React state (via `value` prop and `onChange`), ensuring React is the single source of truth.

**77. What are uncontrolled components?**
Inputs that maintain their own internal state, accessed via refs (e.g., `ref.current.value`) when needed, similar to traditional HTML forms.

**78. How do you manage form state using hooks?**
Use `useState` for each field or a combined state object, update via `onChange` handlers, and optionally `useReducer` for complex forms.

**79. How do you reset a form in React?**

* **Controlled**: Reset state values to initial defaults.
* **Uncontrolled**: Call `formRef.current.reset()`.
* Libraries like Formik provide `resetForm()`.

**80. How do you handle onChange events for checkboxes?**

```jsx
function handleChange(e) {
  const { name, checked } = e.target;
  setForm({ ...form, [name]: checked });
}
<input type="checkbox" name="subscribe" checked={form.subscribe} onChange={handleChange} />
```

---

That completes answers 61–80. Let me know if you need further elaboration or examples!


---

#### 👨‍💻 State Management

**81. What is Redux?**
A predictable state container for JavaScript apps. It centralizes application state in a single store, enforces unidirectional data flow, and uses pure reducers to update state.

**82. What are actions, reducers, and the store in Redux?**

* **Action**: A plain object describing “what happened,” with a `type` and optional payload.
* **Reducer**: A pure function `(state, action) => newState` that takes the current state and an action to produce the next state.
* **Store**: Holds the application state tree, exposes `getState()`, `dispatch()`, and `subscribe()`.

**83. How do you dispatch an action in Redux?**
Call `store.dispatch({ type: 'INCREMENT', payload: 1 })`, or in React use the `useDispatch` hook:

```js
const dispatch = useDispatch();
dispatch({ type: 'ADD_TODO', payload: newTodo });
```

**84. What is Redux Toolkit?**
The official, opinionated, batteries-included toolset for Redux. It simplifies store setup with `configureStore`, reduces boilerplate via `createSlice`, and includes utilities like `createAsyncThunk`.

**85. What is middleware in Redux?**
A function layer between dispatching an action and the moment it reaches the reducer. Middleware can intercept, log, delay, or dispatch other actions. Common examples: `redux-thunk` for async logic, `redux-logger` for logging.

**86. What is the difference between Redux and MobX?**

* **Redux**: Centralized single immutable store, pure reducers, explicit actions, predictable but more boilerplate.
* **MobX**: Observable mutable state with decorators or hooks, less boilerplate, more magic and implicit dependencies.

**87. How do you connect Redux to React components?**

* **Hooks**: Use `useSelector(state => state.someSlice)` to read state and `useDispatch()` to dispatch.
* **Connect HOC**: Wrap components with `connect(mapStateToProps, mapDispatchToProps)`.

**88. What is a thunk in Redux?**
A function that returns another function, used by `redux-thunk` middleware to perform async operations. Thunks receive `(dispatch, getState)` as arguments and can dispatch multiple actions over time.

**89. How do you debug Redux apps?**

* **Redux DevTools**: Inspect action history, state diffs, time travel, and replay.
* **Logging middleware**: Log actions and state snapshots.
* **TypeScript**: Add static typing to catch mistakes in actions and reducers.

**90. What are the benefits of Redux Toolkit over plain Redux?**

* Auto-configured store with good defaults
* Less boilerplate via `createSlice` and `createAction`
* Built-in middleware (thunk, serializability checks)
* Immutability handled under the hood with Immer
* Opinionated patterns that follow best practices

---

#### 🔧 Testing & Debugging

**91. How do you test React components?**

* **Unit tests**: Render components in isolation with React Testing Library or Enzyme.
* **Snapshot tests**: Capture UI output and detect unintended changes.
* **Integration tests**: Simulate user interactions and verify component behavior.

**92. What is Jest?**
A JavaScript testing framework by Meta (formerly Facebook). It provides a test runner, assertion library, mocking, and snapshot testing out of the box.

**93. What is React Testing Library?**
A lightweight testing utility that encourages testing components the way users interact with them by querying DOM by text, role, and accessibility attributes rather than internal implementation.

**94. What is snapshot testing?**
Capturing a serialized version of a component’s rendered output (e.g., its DOM tree) and comparing it to a stored snapshot to catch regressions.

**95. How do you test a form in React?**

* Render the form component,
* Use user-event to type into inputs and click submit,
* Assert that callbacks are called with correct data or that validation messages appear.

**96. How do you mock an API call in tests?**

* **Jest**: Use `jest.mock('apiModule')` to replace fetch functions with mocks, or use `global.fetch = jest.fn()`.
* **MSW (Mock Service Worker)**: Intercept network requests in tests for more realistic behavior.

**97. How do you test hooks?**

* Use **React Hooks Testing Library**’s `renderHook` to render the hook in a test environment and inspect its return values and side effects.
* Wrap with necessary context providers via the `wrapper` option.

**98. What is the difference between unit and integration tests?**

* **Unit tests**: Test a single unit (function or component) in isolation, often mocking external dependencies.
* **Integration tests**: Test multiple units working together, including real logic interaction and UI flows.

**99. What is Enzyme and how is it different from React Testing Library?**

* **Enzyme**: Provides shallow, mount, and static rendering, allowing deep inspection of component internals (state, props, instance methods).
* **React Testing Library**: Emphasizes testing behavior over implementation by querying rendered DOM and encouraging tests that resemble user interactions.

**100. How do you debug performance issues in React?**

* **React DevTools Profiler**: Record commits and measure render durations, identify “hot” components.
* **Performance marks**: Insert `performance.mark` and `performance.measure` around code.
* **Browser tools**: Use Chrome DevTools Performance tab to inspect long tasks, layout thrashing, and memory leaks.
* **Audit re-renders**: Use `why-did-you-render` or React’s built-in “Highlight Updates” feature to spot unnecessary renders.

---

That completes answers for questions 81–100. Let me know if you’d like code samples or deeper explanations!


---

#### 🚧 Tooling & Build

**101. What is Create React App?**
A CLI tool by Facebook to bootstrap React projects with zero-config. It sets up Webpack, Babel, ESLint, dev server, and build scripts out of the box.

**102. What is Webpack and how does React use it?**
A module bundler that processes JS, CSS, and assets into optimized bundles. CRA and custom setups use Webpack to transpile JSX, split code, and hot-reload during development.

**103. What is Babel and why is it needed?**
A JavaScript compiler that transforms modern ES6+/JSX syntax into browser-compatible code. React uses Babel to convert JSX and new language features for older environments.

**104. What are .env files used for?**
Store environment-specific variables (API endpoints, feature flags) outside code. CRA recognizes files like `.env.development` and prefixes keys with `REACT_APP_` to inject into `process.env`.

**105. How do you eject a CRA project?**
Run `npm run eject`. This copies all configuration (Webpack, Babel, ESLint) into your project so you can customize—but it’s irreversible.

**106. How do you set up ESLint in a React project?**

* Install: `npm install eslint --save-dev`
* Initialize: `npx eslint --init` (choose React, ES modules, etc.)
* Add `.eslintrc` with React plugin/config (e.g., `eslint-config-airbnb`), then integrate with your editor and CI.

**107. What is code splitting?**
Dividing your bundle into smaller chunks loaded on demand, reducing initial load. Implemented via dynamic `import()` or React’s `React.lazy` and `<Suspense>`.

**108. How do you configure absolute imports in React?**

* **CRA**: Add a `jsconfig.json` with `"baseUrl": "src"`.
* **Custom Webpack**: Set `resolve.alias` or `resolve.modules` to include your source directory.

**109. How do you optimize bundle size?**

* Tree-shake unused exports.
* Use production mode (`NODE_ENV=production`).
* Code-split routes/components.
* Remove large dependencies or replace with lighter alternatives.
* Compress assets and serve via HTTP/2 with gzip/Brotli.

**110. How do you handle environment variables in React?**
Define `.env.*` files with keys prefixed `REACT_APP_`. Access them in code as `process.env.REACT_APP_API_URL`. Ensure sensitive keys are not exposed in front-end bundles.

---

#### 🚀 Real-world Scenario Questions

**111. How do you fetch data from an API using useEffect?**

```jsx
useEffect(() => {
  let isMounted = true;
  fetch(url)
    .then(res => res.json())
    .then(data => isMounted && setData(data))
    .catch(err => isMounted && setError(err));
  return () => { isMounted = false; };
}, [url]);
```

**112. How would you implement pagination in a table?**

* Keep `page` and `pageSize` in state.
* Fetch or slice data based on those.
* Render page controls (`Prev`, `Next`, page numbers) that update state and re-render.

**113. How do you handle error boundaries in React?**
Create a class component implementing `static getDerivedStateFromError()` and `componentDidCatch()`, render a fallback UI on error, and wrap child components with it.

**114. How would you implement dark mode in a React app?**

* Store theme in context or state.
* Toggle a CSS class on `<body>` or use CSS variables.
* Persist choice in `localStorage`.
* Consume via `useContext` or a custom `useTheme` hook.

**115. How do you handle authentication in a React app?**

* Use context or a state library to store auth tokens.
* On login, store token in memory or secure cookie.
* Attach token to API requests via interceptors.
* Protect routes with private-route components.

**116. How do you create a reusable button component?**

```jsx
function Button({ children, variant = 'primary', ...props }) {
  return (
    <button className={`btn btn-${variant}`} {...props}>
      {children}
    </button>
  );
}
```

Accept props like `onClick`, `disabled`, and styling variants.

**117. How would you integrate a third-party chart library?**

* Install the library (e.g., `npm install chart.js react-chartjs-2`).
* Create a wrapper component that initializes the chart with props/data in `useEffect`.
* Clean up on unmount.

**118. How do you structure a large-scale React application?**

* Organize by feature or domain folders.
* Within each: `components/`, `hooks/`, `services/`, `styles/`.
* Shared utilities and common UI in a top-level `shared` or `ui` folder.
* Maintain a clear import path strategy.

**119. How do you implement a modal popup?**

* Render modal content in a portal (e.g., `ReactDOM.createPortal`) to `document.body`.
* Control visibility via state.
* Trap focus and close on overlay click or ESC.

**120. How do you build a multi-step form in React?**

* Store step index in state.
* Divide form into step components.
* Pass shared form data and update methods via context or prop drilling.
* Render the active step and navigation buttons.

**121. How would you handle file uploads?**

* Use an `<input type="file" />` with `onChange` to capture `File` objects.
* Send via `FormData` in a `fetch` or Axios POST.
* Show progress using the `onUploadProgress` callback (Axios) or XHR events.

**122. How would you create a dashboard with analytics widgets?**

* Define widget components that fetch or receive data props.
* Lay out using a responsive grid (CSS Grid or a library like React Grid Layout).
* Fetch data in parent or via hooks and pass to widgets.

**123. How do you handle session management in a React SPA?**

* Use HTTP-only secure cookies for tokens to mitigate XSS.
* Refresh tokens via silent renewal (e.g., hidden iframe or refresh endpoint).
* Store session state in context or global store.

**124. How do you manage role-based access in components?**

* Store user roles/permissions in context or auth state.
* Create a `<RoleGuard roles={['admin']}>` component that checks and conditionally renders children or redirects.

**125. What are some common performance bottlenecks in React apps?**

* Unnecessary re-renders due to changing props or context.
* Large bundle sizes without code-splitting.
* Rendering long lists without virtualization.
* Blocking operations in rendering (expensive computations).
* Excessive DOM nodes or deeply nested component trees.

---

That covers questions 101–125! Let me know if you’d like more detail or examples on any of these topics.


---

#### 📚 Miscellaneous

**126. What are portals in React?**
Portals let you render children into a DOM node outside the main React root hierarchy. Created via `ReactDOM.createPortal(children, domNode)`, they’re useful for modals, tooltips, and overlays that must escape parent CSS overflow or stacking contexts.

**127. What are fragments and why are they used?**
Fragments (`<React.Fragment>` or `<>…</>`) let you group multiple elements without adding extra DOM nodes, keeping the markup clean and avoiding unnecessary wrappers.

**128. What are forward refs?**
A pattern (`React.forwardRef`) that lets parent components pass a `ref` through to a child’s DOM node or component instance. Useful for building reusable components that expose an internal element to callers.

**129. What are error boundaries?**
Class components implementing `static getDerivedStateFromError()` and `componentDidCatch()` to catch rendering errors in their subtree and display a fallback UI, preventing the entire app from crashing.

**130. What is reconciliation in React?**
The process by which React diffs the previous and next virtual DOM trees, then computes and applies the minimal set of real DOM updates to sync them, based on keys and component types.

**131. How does suspense for data fetching work?**
(Experimental) Wrap components with `<Suspense fallback={…}>`; when a data-fetching component “suspends” (throws a Promise), React shows the fallback until the promise resolves, then retries rendering.

**132. What are transitions in React 18?**
Transitions separate urgent updates (typing, clicks) from non-urgent ones (UI transitions). Use `startTransition` to mark updates as transitional, letting React keep the UI responsive by interrupting or deferring them during high-priority work.

**133. What is concurrent rendering?**
A React 18 feature where rendering can be paused, aborted, or restarted to prioritize urgent updates. It enables smoother UIs by coordinating multiple state updates without blocking the main thread.

**134. What is hydration in React?**
The process of attaching React’s event listeners to server-rendered HTML on the client side, enabling the HTML markup sent from the server to become a fully interactive React app without re-rendering from scratch.

**135. What is the difference between static and dynamic rendering?**

* **Static (SSG)**: HTML generated at build time (e.g., Next.js’s `getStaticProps`), served as prebuilt pages.
* **Dynamic (SSR/CSR)**:

  * **SSR**: HTML generated on each request on the server.
  * **CSR**: HTML is minimal; JavaScript on the client renders the content at runtime.

---

#### 📊 GraphQL & Advanced APIs

**136. What is GraphQL and how does it compare to REST?**
GraphQL is a query language and runtime for APIs that lets clients request exactly the data they need. Unlike REST’s fixed endpoints returning predefined shapes, GraphQL uses a single endpoint with a flexible schema, reducing over- and under-fetching.

**137. How do you use Apollo Client in React?**

* Install `@apollo/client` and wrap your app in `<ApolloProvider client={client}>`.
* Use `useQuery` and `useMutation` hooks in components to run GraphQL operations and manage loading, error, and data states.

**138. How do you perform mutations in GraphQL?**
Define a mutation in your client code:

```graphql
mutation AddTodo($text: String!) {
  addTodo(text: $text) { id, text, completed }
}
```

Then call it with `const [addTodo, { data, loading, error }] = useMutation(ADD_TODO);` and invoke `addTodo({ variables: { text } })`.

**139. How do you handle caching in Apollo?**
Apollo Client uses an in-memory cache normalized by object `__typename` and `id`. You can configure fetch policies (`cache-first`, `network-only`, etc.), write directly to the cache with `cache.writeQuery`, or customize cache behavior via type policies and field policies.

**140. What are subscriptions in GraphQL?**
Long-lived operations that push real-time updates from the server to the client over WebSocket (e.g., using `graphql-ws` or `subscriptions-transport-ws`). In Apollo, use the `useSubscription` hook to subscribe and react to incoming data.

---

Let me know if you’d like deeper dives, code snippets, or examples on any of these topics!


---

#### 🔗 Integration

**141. How do you integrate React with Firebase?**

* Install the Firebase SDK (`npm install firebase`).
* Initialize Firebase in a module with your config (`initializeApp({...})`).
* Use Firebase services (Auth, Firestore, Realtime Database, Storage) via their JS APIs—often wrapped in custom hooks (e.g., `useAuth`) for React.

**142. How do you add authentication with Auth0?**

* Install Auth0 React SDK (`@auth0/auth0-react`).
* Wrap your app in `<Auth0Provider domain={…} clientId={…}>`.
* Use the `useAuth0` hook to log in/out, access user info, and protect routes with conditional rendering or a `PrivateRoute` component.

**143. How do you connect React to a backend like Node.js or Django?**

* Expose REST or GraphQL endpoints in your backend.
* In React, call these APIs via `fetch` or Axios in `useEffect` or custom data hooks.
* Handle CORS by configuring appropriate headers on the server or using a proxy in development.

**144. How do you deploy a React app to Vercel or Netlify?**

* Push your code to GitHub/GitLab.
* On Vercel or Netlify, create a new project connected to your repo.
* Configure the build command (`npm run build`) and publish directory (`build`).
* Deploy—platforms handle building, asset optimization, and CDN distribution automatically.

**145. How do you monitor errors in production apps?**

* Integrate an error-tracking service like Sentry or LogRocket.
* Install its SDK, configure a DSN, and wrap your app in its provider or initialize in your entry file.
* Capture uncaught exceptions and unhandled promise rejections, and view aggregated error reports in the dashboard.

**146. How do you perform SEO for a React SPA?**

* Use server-side rendering (SSR) or static generation to serve pre-rendered HTML (e.g., with Next.js or Gatsby).
* Add meta tags and structured data via React Helmet.
* Generate and submit an XML sitemap.
* Ensure meaningful URLs and fallback content for bots.

**147. What are static site generators with React (e.g., Gatsby)?**
Tools that build HTML at compile time by fetching data and rendering React components into static files. They offer optimized asset pipelines, image processing, and plugins for sourcing markdown, CMSs, and APIs.

**148. What is Next.js and how is it different from CRA?**

* **Next.js**: A React framework supporting SSR, SSG, API routes, file-based routing, and built-in optimizations.
* **CRA**: A client-only starter. CRA bundles a pure SPA without server-rendering or backend routes. Next.js is full-stack and SEO-friendly out of the box.

**149. How do you implement analytics tracking?**

* Install an analytics library (e.g., Google Analytics via `react-ga` or `@vercel/analytics`).
* Initialize in your app’s entry point.
* Track page views on route changes (listen to router events) and custom events in components.

**150. What is server-side rendering (SSR) and how is it done in React?**
SSR generates HTML on the server for each request by rendering React components (using `renderToString` or `renderToNodeStream`), then sends it to the client. Implemented with frameworks like Next.js or custom Express setups using `react-dom/server`, improving initial load performance and SEO.


