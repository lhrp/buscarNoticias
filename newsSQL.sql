--DROP TABLE IF EXISTS noticiasDoDia

--CREATE TABLE noticiasDoDia(
--                             nCdNoticia INT IDENTITY(1,1) NOT NULL
--                           , dExtracaoNoticias DATETIME NOT NULL DEFAULT (GETDATE())
--                           , cTituloNoticia VARCHAR(MAX) NOT NULL
--                           , cLinkNoticia VARCHAR(MAX) NOT NULL
--                           , cNoticia VARCHAR(MAX) NOT NULL
--                           )

SELECT *
  FROM noticiasDoDia
  --FOR JSON AUTO