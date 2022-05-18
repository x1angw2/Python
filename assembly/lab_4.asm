; 向内存 0:200~0:23f 依次写入数据 0~63
assume cs:code

code segment


	mov ax,20h
	mov ds,ax

	mov bl,0
	mov cx,64

s:	mov [bx],bl
	inc bl
	loop s

	mov ax,4c00h
	int 21h

code ends
end
