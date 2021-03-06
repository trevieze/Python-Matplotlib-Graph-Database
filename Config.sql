USE [Datalogging]
GO
/****** Object:  StoredProcedure [dbo].[Config]    Script Date: 06/23/2016 14:18:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Config]
	-- Add the parameters for the stored procedure here
	@x1name VarChar(50),
	@y1name VarChar(50),
	@y2name VarChar(50),
	@y3name VarChar(50),
	@y4name VarChar(50),
	@y5name VarChar(50),
	@y6name VarChar(50),
	@y7name VarChar(50),
	@y8name VarChar(50),
	@xscale real,
	@title VarChar(50),
	@numplots int

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE datalogcfg SET  [x1name] = @x1name , [y1name]= @y1name, [y2name] = @y2name, [y3name] = @y3name, [y4name] = @y4name, [y5name] = @y5name,
		[y6name] = @y6name,	[y7name] = @y7name,	[y8name] = @y8name, [xscale] = @xscale, [title] = @title, [numplots] = @numplots WHERE dataid = 1
END
