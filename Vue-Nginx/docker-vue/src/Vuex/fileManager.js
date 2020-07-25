const fileListManager = {
	filterStat: false,
	sorter: "",
	dirCounter: 0,
	fileCounter: 0,
	starCounter: 0,
	uploadList: [],
	fileList: [],
	nowDir: [0,],
	dirPath: ["云文档", ],
	dirQueue: [],
}

const fileMutations = {	
	CHANGE_CARD: (fileListManager, cardName) => {
		fileListManager.dirPath = [cardName];
	},
	OUTSIDE_DIR: (fileListManager) => {
		if (fileListManager.nowDir.length == 1) return ;
		fileListManager.nowDir.pop();
		fileListManager.dirPath.pop();
	},
	CHANGE_DIR: (fileListManager, i) => {
		fileListManager.nowDir.push(fileListManager.fileList[i].id);
		fileListManager.dirPath.push(fileListManager.fileList[i].name);
	},
	ADD_MKDIR: (fileListManager) => {
		fileListManager.fileCounter++;
	},
	SET_RENAME: (fileListManager, index) => {
		fileListManager.fileList.splice(index, 1, {
			...fileListManager.fileList[index],
			'setRename': true,
		});
	},
	RENAME: (fileListManager, data) => {
		fileListManager.fileList.splice(data.index, 1, {
			...fileListManager.fileList[data.index],
			'setRename': false,
			'name': data.newName,
		})
	},
	SET_FILELIST: (fileListManager, fileList) => {
		var fileType = (type) => {
				switch(type) {
					case 1:
						return "glyphicon-picture";
					case 2: 
						return "glyphicon-inbox";
					case 3:
						return "glyphicon-th";
					case 4:
						return "glyphicon-blackboard";
					case 5:
						return "glyphicon-facetime-video";
					case 100:
						return "glyphicon-folder-close";
					default:
						return "glyphicon-question-sign";
				};
		};
		var starCounter = 0;
		var dirCounter = 0;
		for (let i = 0; i < fileList.length; ++i) {
			if (fileList[i].star) starCounter++;
			if (fileList[i].type == 100) dirCounter++;
			fileList[i] = {
				...fileList[i],
				'icon': fileType(fileList[i].type)
				};
		};
		fileListManager.fileList = fileList;
		fileListManager.dirCounter = dirCounter;
		fileListManager.fileCounter = fileList.length - dirCounter;
		fileListManager.starCounter = starCounter;
	},
	ADD_FILELISTVAR: (fileListManager, dict) => {
		for (let i = 0; i < fileListManager.fileCounter; ++i) {
			fileListManager.fileList[i] = {
				...fileListManager.fileList[i],
				...dict,
			}
		}
	},
	SET_FILTERSTAT: (fileListManager, stat) => {
		fileListManager.filterStat = stat
		for (let i = 0; i < fileListManager.fileList.length; i++) {
			fileListManager.fileList[i].filter = stat;	
		}
	},
	SET_FILTER: (fileListManager, rules) => {
		var filterStat = false;
		if (rules < 0) {
			rules *= -1;
			filterStat = true;
		}
		for (let i = 0; i < fileListManager.fileCounter; i++) {
			if (fileListManager.fileList[i].type == rules) {
				fileListManager.fileList[i].filter = filterStat;	
			}
		}
	},
	SET_SORTER: (fileListManager, rules) => {
		fileListManager.sorter = rules;
	},
	SET_STARFILE: (fileListManager, stat) => {
		if (stat) {
			fileListManager.starCounter++;
		} else {
			fileListManager.starCounter--;
		}
	},
	SET_COUNTER: (fileListManager, num) => {
		fileListManager.fileCounter = num;
	},
	DELETE_FILE: (fileListManager, index) => {
		fileListManager.fileList.splice(index, 1);
		fileListManager.fileCounter--;
	}
}

export { 
	fileListManager,
	fileMutations
};
