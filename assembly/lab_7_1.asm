assume cs:codesg, ds:datasg, ss:stacksg

datasg segment
	db '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983'
	db '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992'
	db '1993', '1994', '1995'																	
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
	db 336 dup (0)						; 21 x 16 = 226 字节
tablesg ends

stacksg segment
	db 0, 0, 0, 0, 0, 0, 0, 0
	db 0, 0, 0, 0, 0, 0, 0, 0
	db 0, 0, 0, 0, 0, 0, 0, 0
	db 0, 0, 0, 0, 0, 0, 0, 0
stacksg ends

codesg segment

	start:	mov ax, datasg
			mov ds, ax
			mov ax, stacksg
			mov ss, ax
			mov sp, 20H
; ------------------------------ 设置 ds 和 ss 
			mov si, 0					; 用于 年份 公司收入 访问变量
			mov di, 0
			mov cx, 21					; 循环次数

			mov ax, 0
			mov dx, 0					; 存放收入数据  ax 和 dx 用于计算
			mov bx, 0					; 存放 雇员人数 
			mov bp, 0

		s:	push ds:[si]				; 读 年份数据
			pop ds:[224 + di]			; 写 年份数据
			push ds:[si + 2]			; 读 年份数据
			pop ds:[226 + di]			; 写 年份数据
; ------------------------------  处理年份数据


			mov ax, ds:[84 + si]		; 读 收入低位
			mov ds:[229 + di], ax		; 写 收入低位
			mov dx, ds:[86 + si]		; 读 收入高位
			mov ds:[231 + di], dx		; 写 收入高位   需要除法计算 注意 ax dx 寄存器
			mov bx, ds:[168 + bp]		; 读 雇员数
			mov ds:[234 + di], bx		; 写 雇员数

; ------------------------------  计算人均收入

			div bx
			mov ds:[237 + di],  ax


			add bp, 2
			add si, 4
			add di, 10h
			loop s

			mov ax, 4c00h
			int 21h


codesg ends

end start

