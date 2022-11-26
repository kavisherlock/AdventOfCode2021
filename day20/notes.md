This was actually a really straightforward problem that I complicated for myself because of my slightly hacky implementation

For some reason, I refused to handle the edge cases a bit more sensibly, such that it either auto-expands the trench when we reach close to the end, or just handles the edge cases when it calculates the index. This ended up with me having some weirdly specific logic, like `n % 2 == 0 ? imageEnhancer[0] : '.'` in my code to handle the edges of the image

Overall, however, my solution did work, for both parts, pretty similarly. Had to play around with the padding of the "infinite" image for part 2 a bit (though, even that I could've technically programatically handled, such that the padding grows if the lit pixels reach the edges). But hey, didn't need to