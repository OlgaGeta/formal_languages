grammar grammatica;

expr: ddl       # ddlExpr
    | dql       # dqlExpr
    | sql       # sqlExpr
    | atom=INT  # numberExpr
    | atom=STR  # strExpr
    ;


ddl:    create
       | drop
       | alter
       | truncate
       | rename
       ;

create: 'CREATE' name=expr '(' pair=terminal ')';
drop: 'DROP' name=expr;
alter: 'ALTER' name=expr 'ADD' '(' pair=terminal ')';
truncate: 'TRUNCATE' name=expr;
rename: 'RENAME' oldname=expr 'TO' newname=expr;



terminal: key=expr ':' value=expr;


dql: select;

select: 'SELECT' key=expr 'FROM' name=expr;


sql:     insert
       | update
       | delete
       ;

insert: 'INSERT' 'INTO' name=expr '(' key=smallterminal')' 'VALUES' '(' value=smallterminal ')';
update: 'UPDATE' name=expr 'SET' key1=expr '=' key1value=expr 'WHERE' key2=expr '=' key2value=expr;
delete: 'DELETE' 'FROM' name=expr 'WHERE' key=expr '=' value=expr;



smallterminal: value=expr;

/// типы данных

STR         : '"' .*? '"' ;
INT         : [0-9]+;
WS          : [ \t]+ -> skip ;
