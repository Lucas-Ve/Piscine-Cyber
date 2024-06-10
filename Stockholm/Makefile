SCRIPT=./Stockholm

all: encrypt

encrypt:
	$(SCRIPT)

decrypt:
	@read -p "Enter the decryption key: " key; \
	$(SCRIPT) -r $$key

decrypt-silent:
	@read -p "Enter the decryption key: " key; \
	$(SCRIPT) -r $$key -s

version:
	@$(SCRIPT) -v

silent:
	$(SCRIPT) -s

help:
	@echo "Help to Makefile :"
	@echo "  make encrypt            Encrypts files in the infection directory"
	@echo "  make silent             Encrypts files in the infection directory without logs"
	@echo "  make decrypt            Decrypts files in the infection directory"
	@echo "  make decrypt-silent     Decrypts files in the infection directory without logs"
	@echo "  make version            Displays the program version"
	@echo "  make help               Display this help message".

.PHONY: encrypt decrypt version help decrypt-silent silent