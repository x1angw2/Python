;  
;   注意  不要从在第一行测试   会被自动刷新覆盖
;
; 在屏幕中间分别显示 绿色 绿底红色 白底蓝色 的字符串 'welcome to masm!'
; 显示内存在 B8000 ~ BFFFF 地址中 
; 一共 FFFFh - 8000h  =  7FFFh = 32767(10)    32768字节 / 1024  = 32KB 
;
; 显存分为 8 页，每页 32KB / 8  = 4KB 

; dosbox 显示区域大小为 25 x 80 = 2000 个字符
; 每个字符占用 2 字节空间 其中一个字节存储 ASCII 码  另一个字节存储该字符的属性 前景色 背景色 高亮 闪烁 属性
; 偶地址放字符  奇地址放属性
; 低地址放字符  高地址放属性
; 一个屏幕占用 2000 x 2 = 4000 个字节
; dosbox 默认情况下显示第一页的数据 B8000 ~ B8F9F  = 4000

;                   7  6  5  4    3     2  1  0  
;                  BL  R  G  B    I     R  G  B
;                高亮    背景    闪烁     前景



;										定位中间
; 1) 行
; 
; 第一页在前 4000 个字节   也就是    B8000   ~    B8F9F  
; 每行 80 个字符  也就是  80 x 2  =  160 字节
; 第一行		[B8 000]  [B8 09F]
; 第二行		[B8 0A0]  [B8 13F]
; 第三行		[B8 140]  [B8 1DF]
; 第四行		[B8 1E0]  [B8 27F]
; 第五行		[B8 280]  [B8 31F]
; 第六行		[B8 xxx]  [B8 xxx]
; 第七行		[B8 xxx]  [B8 xxx]
; 第八行		[B8 xxx]  [B8 xxx]
; 第九行		[B8 xxx]  [B8 xxx]
; 第十行		[B8 xxx]  [B8 xxx]
; 第十一行		[B8 xxx]  [B8 xxx]
; 第十二行		[B8 xxx]  [B8 xxx]
; 第十三行		[B8 780]  [B8 81F]      中间一行    160 x 12  为起始为位置   加 159 (0 开始)  
; 第十四行		[B8 xxx]  [B8 xxx]
; 第十五行		[B8 xxx]  [B8 xxx]
; 第十六行		[B8 xxx]  [B8 xxx]
; 第十七行		[B8 xxx]  [B8 xxx]
; 第十八行		[B8 xxx]  [B8 xxx]
; 第十九行		[B8 xxx]  [B8 xxx]
; 第二十行		[B8 xxx]  [B8 xxx]
; 第二十一行	[B8 xxx]  [B8 xxx]
; 第二十二行	[B8 xxx]  [B8 xxx]
; 第二十三行	[B8 xxx]  [B8 xxx]
; 第二十四行	[B8 xxx]  [B8 xxx]
; 第二十五行	[B8 F00]  [B8 F9F]
; 
; 2) 列
;
;  [00 01]  [02 03]  [04 05] [06 07] ....................... [9E 9F]
;  第一列   第二列   第三列  第四列							第八十列
;  偶数 中间有两列  [78 79]  [80 81]    
;             hex   [4E 4F]  [50 51]
;   welcome[ t]o masm!   空格对应 [4E 4F]   t 对应 [50 51]
; 
;      [40 41]  [42 43]  [44 45]  [46 47]  [48 49] [4A 4B]  [4C 4D]  [4E 4F]  [50 51]  [52 53]  [54 55]  [56 57]  [58 59]  [5A 5B]  [5C 5D]  [5E 5F]
;		 w         e        l        c        o       m        e       [ ]       t        o       [ ]       m        a        s        m        !
; 

assume cs:codesg, ds:datasg

datasg segment
	db 'welcome to masm!'	; 共 16 个字符
	db 2, 24, 71			; 2:绿色    24:绿底红色     71:白底蓝色
datasg ends


codesg segment

	start:	mov ax, datasg
			mov ss, ax
			mov sp, 20h									; 定义栈 存放临时数据  datasg 一共 20h 字节
			mov si,0
			mov di,0

			mov cx,3
		s0: push cx
			mov bx,0
			mov cx,10h									; 合计 16 个字符
		s1: mov ax,datasg
			mov ds,ax
			mov ax,0
			mov al,[bx]									; 内存中取字符到寄存器
			mov ah,ds:[10h+di]								; 取属性

			mov dx,0b87ah  
			mov ds,dx									; 取显存段寄存器

			mov [si],ax
			add si, 2

			inc bx
			loop s1

			inc di
			pop cx
			loop s0


			mov ax, 4c00h
			int 21h

codesg ends

end start

