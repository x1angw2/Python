assume cs:code   ;  假设  cs【命令地址】 指向 code 段
 
code segment
	mov ax,0ffffh  
	mov ds,ax		; 数据段地址设置为 0ffffh
	mov bx,6

	mov al,[bx]    ; al 从 0ffff x 10   + 6   = 0ffff6 取一个字节型数据
	mov ah,0       ; ah 数据设置为 0

	mov dx,0	   ; dx 数据设置为 0

	mov cx,3       ; cx 数据设置为 3   为 循环做准备
s:add dx,ax        ; dx = ax + dx  重复三次   dx = 0   ax = 31   31 + 31 + 31 = 93
	loop s

	mov ax,4c00h
	int 21h

code ends
end
