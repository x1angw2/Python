; 第一个字符改为大写  第二个字符串改为小写


;	大写	 十六进制		 二进制			小写	 十六进制		 二进制
;    A			41			01000001		 a			61			01100001
;    B			42			01000010		 b			62			01100010
;    C			43			01000011		 c			63			01100011
;    D			44			01000100		 d			64			01100100
;    E			45			01000101		 e			65			01100101
;    F			46			01000110		 f			66			01100110
;    G			47			01000111		 g			67			01100111

assume cs:codesg, ds:datasg

datasg segment
	db 'BaSic'
	db 'iNfOrMaTiOn'    ; 在同一个段的数据   首尾相连
datasg ends

; 分别找到两个字符串的地址 第二个 用 and 11011111
;						   第一个 用 or  00100000
codesg segment

	start:	mov ax,datasg
			mov ds,ax

			mov bx,0
			mov cx,5
			
		s:	mov ax,0
			mov al,[bx]
			and al, 11011111b
			mov [bx], al
			inc bx
			loop s

			mov bx,5       ; 之前的 bx 已经是 6 ，需要重新设置为 5
			mov cx,11
		s0:	mov ax,0
			mov al,[bx]
			or al, 00100000b
			mov [bx],al
			inc bx
			loop s0

			mov ax, 4c00h
			int 21h

codesg ends

end start

