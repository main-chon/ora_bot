import asyncio
from datetime import datetime, timedelta

async def schedule_mention(ctx, 시간: str, 이름_리스트: list[str]):
    if '분' in 시간:
        wait_minutes = int(시간.replace('분', ''))
        target_time = datetime.now() + timedelta(minutes=wait_minutes)
    else:
        hour, minute = map(int, 시간.split(':'))
        now = datetime.now()
        target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if target_time < now:
            target_time += timedelta(days=1)

    seconds = (target_time - datetime.now()).total_seconds()

    await ctx.send(f"⏳ {시간}에 멘션 예약 완료! → {', '.join(이름_리스트)}")

    # 수면 대기
    await asyncio.sleep(seconds)

    mentions = []
    not_found = []

    # 1. 직접 멘션된 유저
    for user in ctx.message.mentions:
        mentions.append(user.mention)

    # 2. 입력된 이름으로 서버 전체에서 닉네임 일치 검색
    #    (@ 없는 이름들만 따로 처리)
    이름_텍스트_리스트 = [이름 for 이름 in 이름_리스트 if not 이름.startswith('<@')]
    for 이름 in 이름_텍스트_리스트:
        found_members = [
            member for member in ctx.guild.members
            if member.display_name == 이름
        ]
        if found_members:
            mentions.extend([member.mention for member in found_members])
        else:
            not_found.append(이름)

    if mentions:
        await ctx.send(f"🔔 {', '.join(mentions)} 시간 됐어요!")
    else:
        await ctx.send("🙅‍♂️ 멘션할 유저가 없어요.")

    if not_found:
        await ctx.send(f"⚠️ 못 찾은 이름: {', '.join(not_found)}")