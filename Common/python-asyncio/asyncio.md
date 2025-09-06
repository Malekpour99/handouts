# Asyncio

## Table of Contents

- [Asyncio](#asyncio)
  - [Table of Contents](#table-of-contents)
  - [Core Concepts](#core-concepts)

## Core Concepts

- **Future** -> Futures are like promises in JavaScript, you can `await` them, they will return results.
- **Async Function** -> Any function that is defined using the `async` keyword before it.
- **Coroutine Object** -> Any provoked async function that can be awaited.
- **Task** -> Any scheduled coroutine object in the event loop is a task that enables system to do the context switching.
- **Event Loop** -> A background process for running tasks and enables context switching between them.
