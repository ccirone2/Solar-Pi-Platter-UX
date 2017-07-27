%# info_table.tpl

% rebase('base.tpl')

<main class="main-content">
	<div class="table-wrapper">
		<table id="{{group}}">
			<tr>
				<th colspan="3">{{group}}</th>
			</tr>
	
			%for entry in dict:			
			<tr>
				%for item in entry:
				<th id='row_label'>{{item}}</th>
				
				%if type(entry[item]) == type({'':''}):
				<td id='value'>{{entry[item]['setting']}}</td>
				<td id='control'>
					<input type="button" value={{entry[item]['control'].keys()[0]}} onclick="msg('yay')">
				</td>				
				%else:
				<td id='value'>{{entry[item]}}</td>
				
				%end
				%end
			</tr>
			%end
		</table>
	</div>
</main>
