# 눈싸움 게임 

## 소개
 > 두 명의 플레이어가 참여하는 게임으로, 눈을 던져 맞춰 상대방의 체력을 0으로 만드는 플레이어가 승리하는 게임입니다.

## 게임설명 

**1. 조작법**
>  * player1의 경우 
>    * w : 위로 이동 
>    * s : 아래로 이동
>    * 왼쪽 Shift : 아이템 사용
>    * 왼쪽 Ctrl : 눈 날리기 
>  * player2의 경우
>    * ↑ : 위로 이동
>    * ↓ : 아래로 이동
>    * 오른쪽 Shift : 아이템 사용
>    * 오른쪽 Ctrl : 눈 날리기 

**2. 스텟**
> 스텟은 총 10이 주어지며, 3개의 스텟에 분배할 수 있습니다.
> * 이동 속도 
>   * 기본 이동 속도는 1이며, 스텟 1 증가시 이동 속도가 0.5 증가합니다.
> * 눈 최대 개수
>   * 기본 눈 개수는 0개 이며, 스텟 1 증가시 눈 개수가 1개 증가합니다.
> * 눈 속력 
>   * 기본 눈 속력은 8이며, 스텟 1 증가시 눈 속력이 1 증가합니다. 

**3. 아이템** 
>  * 종류 
>    * 하트 : 사용하면 체력이 1이 회복됩니다.
>    * 방패 : 사용하면 캐릭터 앞에 방어막이 생성되며, 눈에 맞으면 사라집니다.
>    * 독 : 사용하면 상대방의 이동 속도가 느려집니다.
>    * 해독제 : 사용하면 느려진 이동 속도가 회복됩니다.
>   
>  * 아이템 생성 및 획득 방법
>    * 아이템은 10초마다 생성되며, 이미 생성된 아이템이 존재하면 아이템이 생성되지 않습니다.
>    * 아이템은 눈을 맞춰 획득할 수 있으며, 획득한 아이템은 체력 위에 표시됩니다. 
>    * 아이템은 최대 3개까지 보유할 수 있습니다.
>  * 아이템 사용 방법
>    * 아이템은 Shift키로 사용할 수 있으며, 획득한 순서대로만 아이템을 사용할 수 있습니다. 
  

**4. 체력** 
>  * 최대 체력은 3입니다. 
>  * 체력이 0이 되면 게임이 종료됩니다.

## 게임 실행 예시

###1.시작 화면###

![시작화면](image/startscreen.png)
> 해당 이미지는 시작 화면입니다. 게임 시작을 누르면 스탯 분배 화면으로 전환되고, 게임 설명을 누르면 게임 설명 화면으로 전환됩니다.


![게임설명](image/explanationscreen.png)
> 해당 이미지는 게임 설명 화면입니다. 게임 시작을 누르면 게임이 시작됩니다.
 
![스텟분배](image/statscreen.png)
> 해당 이미지는 스텟 분배 화면입니다. 화살표 버튼으로 스텟을 분배할 수 있으며, 게임 시작을 누르면 게임이 시작됩니다.

![게임화면](image/playscreen.png)
> 해당 이미지는 게임 화면입니다. 조작키를 이용해 캐릭터를 조작할 수 있습니다. 

![게임플레이화면](image/playscreen2.png)
> 해당 이미지는 게임 플레이 화면입니다. 화면 하단에 체력과 소유 아이템이 표시됩니다. 아이템을 사용하면 그에 맞는 효과가 나타납니다. 


   
