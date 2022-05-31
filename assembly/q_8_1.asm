; div 计算 data 段中第一个数据除以第二个后的结果，商存在第三个数据的存储单元中
;
; div 指令说明
;	div 内存单元/寄存器 
;	1) 除数分为两种情况
;		1. 除数为 1 个字节
;			被除数默认保存在 ax 中
;			商保存在 al    余数保存在 ah
;		2. 除数为 2 个字节
;			被除数默认保存在 ax 和 dx 中  dx 高位  ax 低位
;			商保存在 ax    余数保存在 dx
;
assume cs:codesg, ds:datasg

datasg segment
	dd 100001   ; 00 00 00 00    00 01 86 a1
	dw 100
	dw 0
datasg ends

codesg segment

	start:	mov ax, datasg
			mov ds, ax
			
			mov bx, 0
			mov ax, [bx]
			mov dx, [bx+2]
			div word ptr [bx + 4]
			mov [bx + 6], ax

			mov ax, 4c00h
			int 21h

	; start:	mov ax, datasg
	; 		mov ds, ax

	; 		mov bx, 0
	; 		mov ax, [bx]
	; 		mov dx, [bx+2]
	; 		div word ptr [bx + 4]
	; 		mov [bx + 6], ax

	; 		mov ax, 4c00h
	; 		int 21h

	; start:	mov ax, datasg
	; 		mov ds, ax

	; 		mov ax, ds:[0]
	; 		mov dx, ds:[2]
	; 		div word ptr ds:[4]
	; 		mov ds:[6],ax

	; 		mov ax,4c00h
	; 		int 21h

codesg ends

end start

