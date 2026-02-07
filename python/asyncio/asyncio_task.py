import asyncio
import time
import argparse
from rich import print as rprint


async def background_worker(name: str, stop_event: asyncio.Event) -> None:
    i = 0
    try:
        while not stop_event.is_set():
            rprint(f"[cyan]\\[bg] {name} tick {i}[/cyan]")
            i += 1
            # wait up to 1s or until stop_event is set
            try:
                await asyncio.wait_for(stop_event.wait(), timeout=1.0)
            except asyncio.TimeoutError:
                continue
    finally:
        rprint(f"[red]\\[bg] {name} exiting[/red]")


async def bad_main() -> None:
    stop_event = asyncio.Event()
    worker = asyncio.create_task(background_worker("worker-1", stop_event))

    try:
        rprint("[green]Main loop running. Press Ctrl-C to stop.[/green]")
        while True:
            rprint("[dim]\\[main] heartbeat[/dim]")
            time.sleep(1)
    except KeyboardInterrupt:
        rprint("[yellow]KeyboardInterrupt received in main()[/yellow]")
    finally:
        rprint("[red]Shutting down: signaling background task to stop[/red]")
        stop_event.set()
        worker.cancel()
        try:
            await worker
        except asyncio.CancelledError:
            pass
        rprint("[green]Shutdown complete[/green]")


async def main() -> None:
    stop_event = asyncio.Event()
    worker = asyncio.create_task(background_worker("worker-1", stop_event))

    try:
        rprint("[green]Main loop running. Press Ctrl-C to stop.[/green]")
        while True:
            rprint("[dim]\\[main] heartbeat[/dim]")
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        rprint("[yellow]KeyboardInterrupt received in main()[/yellow]")
    finally:
        rprint("[red]Shutting down: signaling background task to stop[/red]")
        stop_event.set()
        worker.cancel()
        try:
            await worker
        except asyncio.CancelledError:
            pass
        rprint("[green]Shutdown complete[/green]")


args = argparse.ArgumentParser(description="Asyncio task example")
args.add_argument("--bad", action="store_true", help="Run the bad version that doesn't await the background task")
parsed_args = args.parse_args()

if __name__ == "__main__":
    try:
        if parsed_args.bad:
            asyncio.run(bad_main())
        else:
            asyncio.run(main())
    except KeyboardInterrupt:
        # fallback if interrupted very early
        rprint("[yellow]Interrupted[/yellow]")
