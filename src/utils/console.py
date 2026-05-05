"""
Rich console helpers for OpenLead 1.0
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn
from rich import box

console = Console()

def create_progress():
    """Create a rich progress bar for scraping."""
    return Progress(
        SpinnerColumn(style="white"),
        TextColumn("[bold bright_white]{task.description}"),
        BarColumn(bar_width=40, complete_style="white", finished_style="bright_white"),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    )

def info(msg: str):
    console.print(f"[bright_white]ℹ️  {msg}[/bright_white]")

def success(msg: str):
    console.print(f"[white]✅ {msg}[/white]")

def warning(msg: str):
    console.print(f"[dim]⚠️  {msg}[/dim]")

def error(msg: str):
    console.print(f"[bright_white]❌ {msg}[/bright_white]")

def step(title: str, desc: str = ""):
    console.print(Panel(
        f"[bold]{desc}[/bold]" if desc else "",
        title=f"[bold bright_white]{title}[/bold bright_white]",
        border_style="white",
        box=box.ROUNDED
    ))
