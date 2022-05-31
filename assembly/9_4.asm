assume cs:codesg

datasg segment
	db 0
datasg ends

codesg segment

	start:	mov ax,datasg
			mov ds,ax
			mov bx,0
			jmp word ptr [bx + 1]

codesg ends

end start
