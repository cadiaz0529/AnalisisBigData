import sys, json

#para iterar sobre las fuentes

def main():
	palabra='surcoreanos'
	tipoBusqueda='titulo''

    # Load the data that PHP sent us
    try:
        data = json.loads(sys.argv[1])
    except:
        print "ERROR"
        sys.exit(1)

    # Generate some data to send to PHP
    result = {'status': 'Yes!'}

    # Send it to stdout (to PHP)
    print json.dumps(result)

main()
