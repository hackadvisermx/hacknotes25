# Instalar oh My Zsh en Mac OS con Iterm




brew install zsh zsh-completions

sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
brew cleanup
compaudit | xargs chmod g-w,o-w 
source ~/.zshrc

brew install zsh zsh-autosuggestions
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh

brew install zsh zsh-syntax-highlighting
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
 

## Ver fuentes instaladas 

Catálogo Tipográfico

## Power Level10k o my zsh theme

Meslo Nerd Font.
https://github.com/romkatv/powerlevel10k

## La fuente en la terminal de visualcode

Shift + Command + P
Open Settings (JSON)

"terminal.integrated.fontFamily": "MesloLGS NF"


Referencias
- [Configurar Oh-My-Zsh en Mac OS con iTerm](https://curiotek.com/configurar-oh-zsh-en-mac-os-con-iterm/)
- https://www.freecodecamp.org/news/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38/
- 