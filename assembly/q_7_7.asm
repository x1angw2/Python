; 将 datasg 数据中的每个单词改为大写
assume cs:codesg, ds:datasg

datasg segment
	db 'ibm             '
	db 'dec             '
	db 'dos             '
	db 'vax             '
datasg ends

codesg segment

	start:	mov ax,datasg
			mov ds,ax

			mov cx,4
			mov si,0
			mov bx,0
		s:	mov al,[si+bx]
			and al,11011111b
			mov [si+bx],al
			inc bx

			mov al,[si+bx]
			and al,11011111b
			mov [si+bx],al
			inc bx

			mov al,[si+bx]
			and al,11011111b
			mov [si+bx],al
			mov bx,0

			add si,10h
			loop s

			mov ax,4c00h
			int 21h
			
codesg ends

end start

