import asyncio
from dotenv import load_dotenv

from manager import ResearchManager

async def main() -> None:
    query = input("What would you like to research? ")
    await ResearchManager().run(query)

# .envファイルから環境変数を読み込む
load_dotenv()

if __name__ == "__main__":
    asyncio.run(main())

