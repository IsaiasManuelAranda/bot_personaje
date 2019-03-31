CREATE DATABASE bot_shrek;

USE bot_shrek;

CREATE TABLE personaje (
    id_personaje int auto_increment not null primary key,
    nombre_personaje varchar(30) not null,
    descripcion varchar(2000) not null
);

INSERT INTO personaje(id_personaje, nombre_personaje, descripcion) VALUES
(1, 'shrek', 'Los ogros son como cebollas, capas, las cebollas tienen capas, los ogros tienen capas las cebollas las tienen entiendes?, ambos tienen capas.'),
(2, 'fiona', 'No habeis matado al dragon?'),
(3, 'burro', 'Wow eso si que asusta, y si tu rugido no los espanta tu mal aliento seguro los desmaya, deberias comprar una pastillita de menta, porque el ocico te apesta.'),
(4, 'encantador', 'Ahora no chikistrikis, papi lo discutira luego.'),
(5, 'gengibre', 'De acuerdo, te lo cuento, tu conoces a Pin Pon?, si pin pon, si, se lava su carita con agua y con jabon.'),
(6, 'dragona', 'Es un primor de dragonzuela, uh claro preciosa, ah que ciego fui, eres una dragoncita preciosa.'),
(7, 'gato con botas', 'Por ti beiby, seria batman.'),
(8, 'ada madrina', 'Yo quiero un heroe!'),
(9, 'la hermana fea', 'Bromeas?, es un papucho, su rostro parece tallado por los mismos angeles.');

CREATE USER 'chay'@'localhost' IDENTIFIED BY 'chay';
GRANT ALL PRIVILEGES ON bot_shrek.* TO 'chay'@'localhost';
FLUSH PRIVILEGES;
