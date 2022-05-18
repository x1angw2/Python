; dw 2字节空间 字型数据
; db 1字节空间 字节型数据
; dd 4字节空间 
; 将 a 段和 b 段中的数据相加，结果保存到 c 段中 
assume cs:code, ds:a

a segment
	db 1, 2, 3, 4, 5, 6, 7, 8
a ends

b segment
	db 1, 2, 3, 4, 5, 6, 7, 8
b ends

c segment
	db 0, 0, 0, 0, 0, 0, 0, 0
c ends

; cx 定义循环次数  8
; dx 定义段地址 
; bx 定义偏移地址  步进2
; 从 a 中取数据到寄存器 ax
; 最后将 ax 保存到 c 中

code segment

	start:	mov ax, 0		; 寄存器清零
			mov bx, 0		; 偏移地址步进清零
			mov cx, 8		; loop 次数

			mov dx, a
		s:	mov ds, dx 
			mov ax, [bx]
			
			inc dx
			mov ds, dx
			add ax, [bx]

			inc dx
			mov ds, dx
			mov [bx], ax

			sub dx, 2
			mov ds, dx

			inc bx

			loop s

			mov ax, 4c00h
			int 21h

code ends

end start

