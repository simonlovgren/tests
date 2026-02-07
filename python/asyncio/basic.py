import asyncio
import functools
import inspect
import time

from rich import print as rprint
from rich.markup import escape as rescape

def async_decorator(func):
    """Decorator that supports both async and sync functions.

    If `func` is a coroutine function, returns an async wrapper that awaits
    the function. Otherwise returns a normal wrapper.
    """
    if inspect.iscoroutinefunction(func):
        deco = rescape("[decorator]")
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            rprint(f"[cyan][dim]{deco} Calling async {func.__name__}()[/cyan][/dim]")
            start = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                elapsed = time.perf_counter() - start
                rprint(f"[cyan][dim]{deco} Finished async {func.__name__}() in {elapsed:.3f}s[/cyan][/dim]")

        return async_wrapper

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        rprint(f"[cyan][dim]{deco} Calling sync {func.__name__}()[/cyan][/dim]")
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            rprint(f"[cyan][dim]{deco} Finished sync {func.__name__}() in {elapsed:.3f}s[/cyan][/dim]")

    return sync_wrapper


async def print_after_delay(message: str, delay: float) -> None:
    await asyncio.sleep(delay)
    rprint(f"[blue]{message}[/blue] [dim](delayed by {delay}s)[/dim]")


@async_decorator
async def with_async() -> None:
    rprint("Starting async main function...")
    await print_after_delay("Hello, World!", 2)
    await print_after_delay("Goodbye, World!", 1)
    rprint("Async main function completed.")

@async_decorator
async def with_gather() -> None:
    rprint("Starting async main function with gather...")
    await asyncio.gather(
        print_after_delay("Hello, World!", 2),
        print_after_delay("Goodbye, World!", 1),
    )
    rprint("Async main function with gather completed.")

if __name__ == "__main__":
    asyncio.run(with_async())
    asyncio.run(with_gather())

