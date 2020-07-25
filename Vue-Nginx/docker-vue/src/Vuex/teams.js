const teamFile = {
	teamFileCounter: 0,
	teamFileList: [],
}

const teamFileMutations = {
	setTeamFileList: (teams, fileList) => {
		var fileType = (type) => {
				switch(type) {
					case "text": 
						return "glyphicon-inbox";
					case "sheet":
						return "glyphicon-th";
					case "forShow":
						return "glyphicon-blackboard";
					case "picture":
						return "glyphicon-picture";
					case "video":
						return "glyphicon-facetime-video";
					default:
						return "glyphicon-question-sign";
				};
		};
		for (let i = 0; i < fileList.length; ++i) {
			var counter = 0;
			if (fileList[i].star) counter++;
			fileList[i] = {
				...fileList[i],
				'icon': fileType(fileList[i].type)
				};
		};
		teams.teamFileList = fileList;
		teams.teamFileCounter = fileList.length;
	},
	addTeamFileListVar: (teams, dict) => {
		for (let i = 0; i < teams.teamFileCounter; ++i) {
			teams.teamFileList[i] = {
				...teams.teamFileList[i],
				...dict,
			}
		}
	},
}

const teams = {
	teamBoxState: "initBox",
	teamId: -1,
	teamName: "",
	teamOwner: "",
	teamCounter: 0,
	teamList: [],
	followTeamCounter: 0,
	followTeamList: [],
	...teamFile,
}

const teamsMutations = {
	setFollowTeamList: (teams, teamList) => {
		teams.followTeamList = teamList;
		teams.followTeamCounter = teamList.length;
	},
	setTeamList: (teams, teamList) => {
		teams.teamList = teamList;
		teams.teamCounter = teamList.length;
	},
	setInitBox: (teams) => {
		teams.teamId = -1;
		teams.teamName = "";
		teams.teamBoxState = "initBox";
	},
	setTeamBox: (teams, team) => {
		teams.teamBoxState = "teamBox";
		teams.teamId = team.teamId;
		teams.teamName = team.teamName;
		teams.teamOwner = team.teamOwner;
	},
	...teamFileMutations,
}

export {
	teams,
	teamsMutations,
}
