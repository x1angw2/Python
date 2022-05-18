; 将 datasg 数据中的每个单词的第一个字符改为大写
assume cs:codesg, ds:datasg

datasg segment
	db '1. file         '
	db '2. edit         '
	db '3. search       '
	db '4. view         '
	db '5. options      '
	db '6. help         '
datasg ends

codesg segment

	start:	mov ax,datasg
			mov ds,ax

			mov cx,6
			mov si,0
		s:	mov al,[si+3]
			and al,11011111b
			mov [si+3],al
			add si,10h
			loop s

			mov ax,4c00h
			int 21h
			
codesg ends

end start

