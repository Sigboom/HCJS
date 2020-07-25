const knowNet = {
	nodeCounter: 0,
	nodeList: [],
}

const nodeMutations = {
	SET_NODELIST: (knowNet, nodeList) => {
		knowNet.nodeList = nodeList;
		knowNet.nodeCounter = nodeList.length;
	},
}

export { 
	knowNet,
	nodeMutations,
};
