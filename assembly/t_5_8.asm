; 将内存中 ffff:0~ffff:b 的内容复制到 0:200~0:20b 中
; 0:200~0:20b 和 20:0~20:b 表示同一个地址
; 0 x 10 + 200 = 200     20 x 10 + 0 = 200
; 0 x 10 + 20b = 20b     20 x 10 + b = 20b      节约一个寄存器,两个偏移地址相同
assume cs:code
code segment

	mov ax,0ffffh
	mov ds,ax

	mov bx,0
	mov cx,12

	mov dx,0
	mov ss,dx
	mov sp,12

s:	push [bx]
	inc bx
	loop s

	mov ax,4c00h
	int 21h

code ends
end
