from discord.ext import commands
from utils.mention import schedule_mention

@commands.command(name="멘션")
async def mention(ctx, 시간: str = None, *, 내용: str = None):
    # 사용법 안내
    if 시간 is None or 내용 is None:
        await ctx.send(
            "📌 **멘션 명령어 사용법**\n"
            "`|멘션 21:30 @김현우, 김준수` → 해당 시간에 멘션\n"
            "`|멘션 5분 김현우` → 5분 뒤에 멘션\n\n"
            "이름은 닉네임 기준이며 `@멘션`하면 정확하게 작동해요!"
        )
        return

    이름_리스트 = [이름.strip() for 이름 in 내용.split(',')]
    await schedule_mention(ctx, 시간, 이름_리스트)