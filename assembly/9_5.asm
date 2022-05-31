assume cs:codesg

datasg segment
	dd 12345678h
datasg ends

codesg segment

	start:	mov ax,datasg
			mov ds,ax
			mov bx,0
			mov [bx],bx
			mov [bx+2],cs
			jmp dword ptr ds:[0]

codesg ends

end start
