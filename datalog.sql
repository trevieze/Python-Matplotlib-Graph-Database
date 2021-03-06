USE [Datalogging]
GO
/****** Object:  Table [dbo].[datalog]    Script Date: 06/23/2016 14:16:06 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[datalog](
	[x1] [real] NULL,
	[y1] [real] NULL,
	[y2] [real] NULL,
	[y3] [real] NULL,
	[y4] [real] NULL,
	[y5] [real] NULL,
	[y6] [real] NULL,
	[y7] [real] NULL,
	[y8] [real] NULL,
	[datestamp] [datetime] NULL CONSTRAINT [DF_datalog_datestamp]  DEFAULT (getdate()),
	[dataid] [bigint] IDENTITY(1,1) NOT NULL
) ON [PRIMARY]
