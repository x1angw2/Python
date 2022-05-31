
; Power idea 公司从 1975 年成立一直到 1995 年的基本情况
; 计算出该公司每年的人均收入情况(取整)
; 将结果通过表格的形式写入 tablesg 

assume cs:codesg, ds:datasg, es:tablesg

datasg segment
	db '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983'
	db '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992'
	db '1994', '1994', '1995'
	; 21 年的 21 个字符串  
	; 21 x 4 = 84 字节
	
	dd 16, 22, 382, 1356, 2390, 8000, 16000, 24486, 50065, 97479, 140417, 197514
	dd 345980, 590827, 803530, 1183000, 1843000, 2759000, 3753000, 4649000, 5937000
	; 21 年公司总收入的 21 个dword 型数据
	; 21 x 4 = 84 字节

	dw 3, 7, 9, 13, 28, 38, 130, 220, 476, 778, 1001, 1442, 2258, 2793, 4037, 5635, 8226
	dw 11542, 14430, 15257, 17800
	; 21 年公司雇员人数的 21 个 word 型数据
	; 21 x 2 = 42 字节

datasg ends

tablesg segment
;
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		|           | 年份      | 空格 | 收入 | 空格 | 雇员数 | 空格 | 人均收入 | 空格 |
;       |           |  0 1 2 3  |   4  | 5678 |  9   | a  b   |   c  |  d   e   |   f  |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		| table:0   | '1 9 7 5' |      | 16   |      | 3      |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		| table:10h | '1 9 7 6' |      | 22   |      | 7      |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		| table:20h | '1 9 7 7' |      | 382  |      | 9      |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		| table:30h | '1 9 7 8' |      | 1356 |      | 13     |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		| table:40h | '1 9 7 9' |      | 2390 |      | 28     |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		| table:50h | '1 9 8 0' |      | 8000 |      | 38     |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;			 .            .               .              .                .
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;		|table:140h | '1 9 9 5' |      |593700|      | 17800  |      | ?        |      |
;		|-----------+-----------+------+------+------+--------+------+----------+------|
;
	db 336 dup (0)
tablesg ends

codesg segment

	start:	mov ax, datasg
			mov ds, ax
			
			mov ax, tablesg
			mov es, ax

			mov cx, 21
			mov si, 0
			mov di, 0
; -------------------------------------------------------------
		s:	mov ax, [si]
			mov es:[0], ax

			mov ax, [si + 2]
			mov es:[2], ax					; 年份
; -------------------------------------------------------------
			mov bx, si

			mov ax, si
			add ax, 84
			mov si, ax

			mov ax, [si]
			mov es:[5], ax

			mov dx, [si + 2]
			mov es:[7], dx

			div word ptr [168 + di]			; 计算人均收入
			mov es:[0dh], ax				; 保存人均收入

			mov si, bx						; 收入
; -------------------------------------------------------------
			mov ax,[168+di]
			mov es:[0ah], ax				; 雇员数
; -------------------------------------------------------------

			mov ax, es
			add ax, 1
			mov es, ax
			add si, 4
			add di, 2
			loop s

			mov ax, 4c00h
			int 21h
codesg ends

end start

