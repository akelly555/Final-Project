

var bLineupChanged	= false;

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
function ConvertPosStringToID(Pos)
{
	var iResult	= -1;
	switch (Pos)
	{
		case "C":
			iResult = 2; break;
		case "1B":
			iResult = 3; break;
		case "2B":
			iResult = 4; break;
		case "3B":
			iResult = 5; break;
		case "SS":
			iResult = 6; break;
		case "LF":
			iResult = 7; break;
		case "CF":
			iResult = 8; break;
		case "RF":
			iResult = 9; break;
		case "DH":
			iResult = 10; break;
		default:					
			iResult = -1; break;
	}
	
	return (iResult);
}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
function SetLineup(TeamID, Team, UseDH, PlayerCount)
{
	var bValid		= true;
	var iIndex		= 0;
	var strSlot		= [-1,-1,-1,-1,-1,-1,-1,-1,-1];
	var strPosition	= ['X','X','X','X','X','X','X','X','X'];
	var strNames	= ['','','','','','','','',''];
	var bPosition	= [0,0,0,0,0,0,0,0,0];
	var pItemPos;
	var pItemBO;
	var pItemPlayerID;
	var pItemPlayerName;
	var iPosition	= 0;
	var iBO			= 0;
	var iPlayerID	= -1;
	
	for (iIndex = 0; iIndex < PlayerCount; iIndex++)
	{	
		pItemPos		= document.getElementById("Pos_" + iIndex);
		pItemBO			= document.getElementById("BO_" + iIndex);
		pItemPlayerID	= document.getElementById("PlayerID_" + iIndex);
		pItemPlayerName	= document.getElementById("PlayerName_" + iIndex);

		iPosition	= ConvertPosStringToID(pItemPos.options[pItemPos.selectedIndex].text);
		iBO			= pItemBO.options[pItemBO.selectedIndex].text;
		iPlayerID	= pItemPlayerID.value;

		if (iBO != '--')
		{
			//the player is listed as being in the lineup...
			if (strSlot[iBO-1] == -1)
			{				
				if (iPosition == -1)
				{
					//invalid position value...
					bValid	= false;
					break;
				}
				else if (bPosition[iPosition] == 1)
				{
					//position already filled...
					bValid	= false;
					break;
				}
				else
				{
					//first player at this position...
					bPosition[iPosition]	= 1;
					strSlot[iBO-1]			= iPlayerID;
					strPosition[iBO-1]		= pItemPos.options[pItemPos.selectedIndex].text;					
					strNames[iBO-1]			= pItemPlayerName.innerHTML;
				}		
			}
			else
			{
				//multiple players in same lineup slot...
				bValid	= false;
				break;
			}
		}
	}

	if (bValid == true)
	{
		//this sucks, but we have to tie this page with it's parent.		
		var PlayerIDList	= '';
		var PosList			= '';
		var PlayerNameList	= '';
		var iMaxSlot	= 8;
		
		if ((UseDH == "True") || (UseDH == "true"))
		{
			iMaxSlot	= 9;
		}
		
		for (iIndex = 0; iIndex < (iMaxSlot-1); iIndex++)
		{
			PlayerIDList	= PlayerIDList + strSlot[iIndex] + ';';
			PosList			= PosList + strPosition[iIndex] + ';';
			PlayerNameList	= PlayerNameList + strNames[iIndex] + ';';
		}
		PlayerIDList	= PlayerIDList + strSlot[iMaxSlot-1];
		PosList			= PosList + strPosition[iMaxSlot-1];
		PlayerNameList	= PlayerNameList + strNames[iMaxSlot-1];
		
		if (Team == 'H')
		{
			opener.document.getElementById("hlid").value	= PlayerIDList;
			opener.document.getElementById("hlpos").value	= PosList;
			opener.document.getElementById("hlname").value	= PlayerNameList;
		}
		else
		{
			opener.document.getElementById("vlid").value	= PlayerIDList;
			opener.document.getElementById("vlpos").value	= PosList;
			opener.document.getElementById("vlname").value	= PlayerNameList;
		}
		opener.document.getElementById("setLineup").value = TeamID;
		opener.document.getElementById("formsim").submit();
		window.close();
	}
	else
	{
		alert("The lineup contains errors.  Please make sure there is only 1 player in each lineup slot and a player has been assigned at each position.");
	}
}

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
function CloseMe()
{
	if (bLineupChanged == true)
	{
		if (confirm("Changes have been made to the lineup -- are you sure you want to exit without saving?") == true)
			window.close();
	}
	else	
		window.close();
}
