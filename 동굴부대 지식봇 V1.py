import discord
import asyncio
import random

from discord.utils import get


client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('동굴!')
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content == "/동굴아":
        await message.channel.send(f"동굴이랑 대화하고 싶다면 동굴아 도움말 입력해주세요.")

    if message.content =='/육사교장':
        await message.channel.send('sksksksksksksadjc')

    if message.content =='/제작자':
        await message.channel.send('Kim_ChunSic')

    if message.content =='/봇제작자':
        await message.channel.send('지훈이의 철도새상#7881')

    if message.content =='/도움말':
        await message.channel.send('대화를 하실려면 "동굴아 육사교장" 이런식으로 입력해주세요.')

    if message.content =='/개발자유튜브':
        await message.channel.send('https://www.youtube.com/c/%EB%B0%95%EC%8B%9D%EC%82%AC%EC%9D%B4')
    
    if message.content =='/화랑':
        await message.channel.send('화랑! 소위, korea_hyosus')

    if message.content =='/동굴!':
        await message.channel.send('동굴!')        

    if message.content =='/육사규칙':
        await message.channel.send('1.다른사름을 비하하지 않는다어길시 징게위원회 송치조치. 2.하관이 상관,동료 한테 반말하지 않는다 어길시 경고 1 을 지급한다. 3.인게임이든 디코든 군기문란(애교)=군기없는 챗(ex: 아잉,빠잉,하응) 을 하지않는다. 어길시 경고 2을 지급한다. 4.인게임이든,디코든  욕설을 사용하지 않는다어길시 경고 3 을 지급한다. ')       
       
    if message.content =='/제식':
        await message.channel.send('Face Test Start. 페이스 시험이 시작한걸 알린다. (Face Test Start.를 하지 않고 페이스를 하면 Fake. 이다.)  Right face. 오른쪽으로 90도   Left face. 왼쪽으로 90도   Right incline. 오른쪽으로 45도      Left incline. 왼쪽으로 45도    About face. 180도 회전    Control face. 호스트 바라보기 (Control face.를 한 후 Center face.를 하지 않고 다른걸 하면 Fake.이다.)  Center face. 정면 바라보기 (대각선일때는 Fake. 이다.) Face Test End. 페이스 시험이 종료된걸   알린다.(Face Test Start.를 한 후 Face Test End.를 하지 않고 페이스 외의 제식을 하면 Fake. 이다.)  SF L on me. 호스트 뒤로 1줄로 서기.STS on me. 호스트 양쪽 어깨 맞대고 서기.  DF L on me 호스트 뒤로 2줄로 서기. PTS, Sir. 훈련이나 시험 중 질문이 있을때 사용한 후 호스트에게 허락을 받고 사용한다 [예 : (훈련생 : PTS, Sir. 호스트 : Speak. 훈련생 : 질문)]  Column on me. 말한사람 기준 뒤로 1줄로 서기  Double Column. 말한사람 기준 뒤로 2줄로 서기. Wedge on me. 말한사람 기준 뒤로 날개대형 만들기.  Left echelon on me. 말한사람 기준 뒤로 왼쪽 날개 대형 만들기. (Left wedge on me.도 가능하다.)Right echelon on me. 말한사람 기준 뒤로 오른쪽 날개 대형 만들기. (Right wedge on me.도 가능하다.)  Front wall on me. 말한사람 기준 앞으로 벽만들기. (시선은 호스트방향 정면)Back wall on me. 말한사람 기준 뒤로 벽만들기. (시선은 호스트방향 정면)Box on me. 말한사람 기준으로 둘러싸기 시선은 밖을 향하게. Hold gun(s.) 총 들어. (1명일때는 s를 붙이지 않는다.) Stand. 서서 쏴. (격발하진 않고 행동만 한다.)Crouch. 앉아 쏴. (격발하진 않고 행동만 한다.) Prone. 엎드려 쏴. (격발하진 않고 행동만 한다.)Prepare All bullets. 모든총알 준비. (한탄창) Prepare a bullet. (1발 준비.)Prepare # bullets. (#발 준비.)Aim. 조준.Fire. 사격.Cease fire. 사격 중지.Down gun(s.) 총 내려. (1명일때는 s를 붙이지 않는다.) SF L on me.( 호스트뒤로 1줄로 서기)Prepare, Forward, March! (출발) Halt. (정지) STS on green line. (초록선에 서기)Ready,Set,Begin! (obby 시작)Done, sir. (obby를 다 깬뒤 Done,sir. 이라고 한다) ')

    if message.content =='/육사교가':
        await message.channel.send('동해수구비 감아 금수 내 조국유구 푸른 그 슬기 빛발을 돋혀풍진노도 헤쳐나갈 배움의 전당무쇠같이 뭉치어진 육사 불꽃은모진 역사 역역히 은보래치리아아 영용 영용인제 앞에도 한결 같아라온 누리 소리모아 부르네그 이름 그 이름 우리 육사아사달 기리 누려 여기 반만년변함없는 그 기상 하늘을 내쳐천추만리 바람곁은 이야기하리백사고쳐 쓰러져도 육사혼이야가고 오지 않으니 오질 않으니아아 영용 영용이제도 앞에도 한결 같아라온 누리 소리모아 부르네그 이름 그 이름 우리 육사 ')

client.run("OTgwNDY2NzYyNzE1ODk3ODU2.G4cIPI.h5zrQ13EVA9lCaBlHXiHhHwa-XF7hGTUODlxOk")