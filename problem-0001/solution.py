def main():
    print sum(i for i in xrange(1,1000) if not i % 3 or not i % 5)

if __name__ == '__main__':
    main()
