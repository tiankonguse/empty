#include <stdio.h>
#include <time.h>

#include "coroutine.h"

int
producer(coroutine_t *c, char *r)
{
	coroutine_nodefine(c);
	coroutine_began(c);

	memcpy(r, "hello", strlen("hello"));
	coroutine_yield(c, 0);

	memcpy(r, "world", strlen("world"));
	coroutine_ended(c, 0);
}

int
consumer(coroutine_t *c, char *foo)
{
	coroutine_t *c2;

	/* code in here will execute every time */

	/*
	 * init and allocate sizeof(*v) memory
	 * coroutine_define is only support fix length type pointer
	 */
	coroutine_define(c, c2);

	/* code in here will execute every time */

	coroutine_began(c);	/* setup coroutine execute switch-case */

	/* code in here only execute in first time */

	coroutine_init(c2);
	while (coroutine_next(c2)) {
		coroutine_yield(c, producer(c2, foo + strlen(foo)));	/* case 1 */
	}
	coroutine_deinit(c2);

	coroutine_init(c2);
	while (coroutine_next(c2)) {
		coroutine_yield(c, producer(c2, foo + strlen(foo)));	/* case 2 */
	}
	coroutine_deinit(c2);

	coroutine_ended(c, 0);	/* finish up switch-case and release *c2 */
}

int
main(void)
{
	char foo[64];

	coroutine_t c;
	coroutine_init(&c);
	memset(foo, 0, sizeof(foo));
	
	while (coroutine_next(&c)) {
		consumer(&c, foo);
		printf("foo: %s\n", foo);
	}
	coroutine_deinit(&c);
}
