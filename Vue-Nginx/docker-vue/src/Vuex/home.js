const friends = {
	talkBoxState: "initBox",	
	talkTo: -1,
	talkToName: "",
	followerCounter: 0,
	followingCounter: 0,
	folllowerList: [],
	folllowingList: [],
}

const home = {
	headerIndex: 0,
	userMenuIndex: 0,
	...friends,
}


const friendsMutations = {
	addToTeam: (friends, user) => {
		var index = friends.followerList.indexOf(user);
		if (index != -1) {
			friends.followerList.splice(index, 1, {
				...friends.followerList[index],
				'inTeam': true,
			})
		} else {
			console.log(friends.followerList);
		}
		index = friends.followingList.indexOf(user);
		if (index != -1) {
			friends.followingList.splice(index, 1, {
				...friends.followingList[index],
				'inTeam': true,
			})
		} else {
			console.log(friends.followingList);
		}
	},
	moveToTeam: (friends, user) => {
		var index = friends.followerList.indexOf(user);
		if (index == -1) {
			friends.followerList.splice(index, 1, {
				...friends.followerList[index],
				'inTeam': false,
			})
		} else {
			console.log(friends.followerList);
		}
		index = friends.followingList.indexOf(user);
		if (index) {
			friends.followingList.splice(index, 1, {
				...friends.followingList[index],
				'inTeam': false,
			})
		} else {
			console.log(friends.followingList);
		}
	},
	setFollowerList: (friends, followList) => {
		friends.followerList = followList;
		friends.followerCounter = followList.length;
	},
	setFollowingList: (friends, followList) => {
		friends.followingList = followList;
		friends.followingCounter = followList.length;
	},
	setTalkBox: (friends, data) => {
		friends.talkBoxState = data.box;
		friends.talkTo = data.userId;
		friends.talkToName = data.userName;
	},
	addFollowerCounter: (friends) => {
		friends.followerCounter++;
	}
}

const homeMutations = {
	setHeaderIndex: (home, data) => {
		home.headerIndex = data;
	},
	setUserMenuIndex: (home, data) => {
		home.userMenuIndex = data;
	},
	...friendsMutations,
}


export {
	home,
	homeMutations,
}
