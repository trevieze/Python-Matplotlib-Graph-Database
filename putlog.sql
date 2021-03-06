USE [Datalogging]
GO
/****** Object:  StoredProcedure [dbo].[PutLog]    Script Date: 06/23/2016 14:19:10 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[PutLog]
	-- Add the parameters for the stored procedure here
	@x1 real,
	@y1 real,
	@y2 real,
	@y3 real,
	@y4 real,
	@y5 real,
	@y6 real,
	@y7 real,
	@y8 real

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO datalog (x1, y1, y2, y3, y4, y5, y6, y7, y8) 
		VALUES (@x1, @y1, @y2, @y3, @y4, @y5, @y6, @y7, @y8);
END


