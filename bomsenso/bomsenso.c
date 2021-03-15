#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Daniel Menelkir <menelkir@itroll.org>");
MODULE_DESCRIPTION("Modulo de Bom Senso");
MODULE_VERSION("1.0");

static char *name = "bomsenso";
module_param(name, charp, S_IRUGO);
MODULE_PARM_DESC(name, "Modulo de Bom Senso ativado");

static int __init bomsenso_init(void) {
	printk(KERN_INFO "Bom Senso ativado, agora tudo vai funcionar bem.\n");
 	return 0;
}

static void __exit bomsenso_exit(void) {
	printk(KERN_INFO "Descarregando o bom senso. Vai pra puta que te pariu, seu filho duma puta!\n");
}

module_init(bomsenso_init);
module_exit(bomsenso_exit);
