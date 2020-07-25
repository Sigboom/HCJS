const Header = ()=>import('@/components/public/Header')
const Footer = ()=>import('@/components/public/Footer')
const Setter = ()=>import('@/components/setter/Setter')
const setterView = ()=>import('@/components/setter/views/setter')
const userMenuCard = ()=>import('@/components/home/cards/userMenu')

const setter = {
	path: '/setter', components: {
		header: Header,
		main: Setter,
		footer: Footer,
		default: Setter,
	},
	children: [{
		path: '',
		components: {
			menu: userMenuCard,
			views: setterView,
			default: setterView,
		},
		children: [{
			path: '', name: 'setChoose', meta: { requireAuth: true },
			components: {
			}
		}]
	}]
}

export default setter
