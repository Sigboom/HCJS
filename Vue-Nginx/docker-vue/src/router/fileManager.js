const Header = ()=>import('@/components/public/Header')
const Footer = ()=>import('@/components/public/Footer')
const FileManager = ()=>import('@/components/fileManager/FileManager')
const fileManagerView = ()=>import('@/components/fileManager/views/fileManager')
const fileLoadView = ()=>import('@/components/fileManager/views/fileLoad')
const userMenuCard = ()=>import('@/components/home/cards/userMenu')
const cloudFilesCard = ()=>import('@/components/fileManager/cards/cloudFiles')
const starFilesCard = ()=>import('@/components/fileManager/cards/starFiles')
const shareFilesCard = ()=>import('@/components/fileManager/cards/shareFiles')
const uploadCard = ()=>import('@/components/fileManager/cards/upload')
const downloadCard = ()=>import('@/components/fileManager/cards/download')

const fileManagerRouter = {
	path: '/fileManager',
	components: {
		header: Header,
		main: FileManager,
		footer: Footer,
		default: FileManager,
	},
	children: [{
		path: '',
		components: {
			menu: userMenuCard,
			views: fileManagerView,
			default: fileManagerView,
		},
		children: [{
			path: '', name: 'fileDefault', meta: { requireAuth: true },
			components: {
				cloudFiles: cloudFilesCard,
				starFiles: starFilesCard,
				shareFiles: shareFilesCard,
			}
		}]
	}, {
		path: 'files',
		components: {
			menu: userMenuCard,
			views: fileManagerView,
			default: fileManagerView,
		},
		children: [{
			path: '', name: 'cardChoose', meta: { requireAuth: true },
			components: {
				cloudFiles: cloudFilesCard,
				starFiles: starFilesCard,
				shareFiles: shareFilesCard,
			}
		}]
	}, {
		path: 'fileLoad',
		components: {
			menu: userMenuCard,
			views: fileLoadView,
			default: fileManagerView,
		},
		children: [{
			path: '', name: 'loadPlace', meta: { requireAuth: true },
			components: {
				upload: uploadCard,
				download: downloadCard,
				default: uploadCard,
			}
		}]
	}]
}

export default fileManagerRouter
