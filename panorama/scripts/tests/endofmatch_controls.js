
	options = options + ',' + elMode.GetSelected().id;

	var elTeam = $.GetContextPanel().FindChildTraverse( 'eom-test-player-team' );
	options = options + ',' + elTeam.GetSelected().id;

	var elCharacter = $.GetContextPanel().FindChildTraverse( 'eom-test-player-character' );
	options = options + ',' + elCharacter.GetSelected().id;

	$.DispatchEvent( 'EndOfMatch_Shutdown' );
	          
	                                                   
	          
}
