#ifndef __COROUTINE_H__
#define __COROUTINE_H__

/* The credit belongs to Tom Duff and Simon Tatham */

#include <stdlib.h>
#include <string.h>

typedef struct coroutine {
	int   init;
	int   finished;

	int   line;
	void *vars;
} coroutine_t;

#define coroutine_nodefine(c)					\
	do {							\
		if ((c)->init == 0) {				\
			(c)->init = 1;				\
			(c)->line = 0;				\
		}						\
	} while (0)

#define coroutine_define(c,a)					\
	do {							\
		if ((c)->init == 0) {				\
			(c)->init = 1;				\
			(c)->line = 0;				\
			(c)->vars = malloc(sizeof(*(a)));	\
		}						\
		(a) = (c)->vars;				\
	} while (0)

#define coroutine_began(c)					\
	if ((c)->init == 1)					\
		switch ((c)->line) {				\
		case 0:
			
#define coroutine_yield(c,r)					\
	do {							\
		(c)->line = __LINE__;				\
		return (r);					\
		case __LINE__:;					\
	} while (0)

#define coroutine_return(c,r)					\
	do {							\
		free((c)->vars);				\
		(c)->vars = NULL;				\
		(c)->finished = 1;				\
		return (r);					\
	} while (0)

#define coroutine_ended(c,r)					\
	}							\
	free((c)->vars);					\
	(c)->vars = NULL;					\
	(c)->finished = 1;					\
	return (r)

#define coroutine_init(c)					\
	do {							\
		(c)->init     = 0;				\
		(c)->finished = 0;				\
		(c)->line = 0;					\
		(c)->vars = NULL;				\
	} while (0)

#define coroutine_next(c)					\
	(!(c)->finished)

#define coroutine_deinit(c)					\
	do {							\
		free((c)->vars);				\
		(c)->vars = NULL;				\
	} while (0)

#endif /* __COROUTINE_H__ */
