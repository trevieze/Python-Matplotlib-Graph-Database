USE [Datalogging]
GO
/****** Object:  Table [dbo].[datalogcfg]    Script Date: 06/23/2016 14:16:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[datalogcfg](
	[x1name] [nvarchar](50) NULL,
	[y1name] [nvarchar](50) NULL,
	[y2name] [nvarchar](50) NULL,
	[y3name] [nvarchar](50) NULL,
	[y4name] [nvarchar](50) NULL,
	[y5name] [nvarchar](50) NULL,
	[y6name] [nvarchar](50) NULL,
	[y7name] [nvarchar](50) NULL,
	[y8name] [nvarchar](50) NULL,
	[xscale] [real] NULL,
	[title] [nvarchar](50) NULL,
	[numplots] [int] NULL,
	[dataid] [bigint] IDENTITY(1,1) NOT NULL
) ON [PRIMARY]
