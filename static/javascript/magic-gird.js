let magicGrid = new MagicGrid({
    container: '.container',
    animate: true,
    gutter: 12,
    static: true,
    useMin: true,
});

let masonrys = document.getElementsByTagName("img");

for (let i = 0; i < masonrys.length; i++) {
    masonrys[i].addEventListener('load', function() {
        magicGrid.positionItems();
    }, false);
}

magicGrid.listen();