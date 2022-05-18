; loop [bx]
; 计算 ffff:0 ~ ffff:b 单元中的数据的和 结果保存到 dx 中 
assume cs:code
code segment

	mov ax,0ffffh
	mov ds,ax

	mov ax,0
	mov bx,0
	mov dx,0
	mov cx,12

s:	mov al,[cx]
	add dx,ax
	mov bl,0
	loop s

	mov bl,[0]
	add dx,bx

	mov ax,4c00h
	int 21h

code ends
end
