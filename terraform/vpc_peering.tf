# Create the peer VPC

resource "aws_vpc" "peer" {
  cidr_block           = "10.1.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-peer-vpc"
    }
  )
}

# Create the peer public subnet

resource "aws_subnet" "peer_public" {
  vpc_id = aws_vpc.peer.id

  cidr_block              = "10.1.1.0/24"
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-peer-public-subnet"
    }
  )
}

# Create the peer internet gateway

resource "aws_internet_gateway" "peer" {
  vpc_id = aws_vpc.peer.id

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-peer-igw"
    }
  )
}

# Create the peer route table

resource "aws_route_table" "peer_public" {
  vpc_id = aws_vpc.peer.id

  route {
    cidr_block = "0.0.0.0/0"

    gateway_id = aws_internet_gateway.peer.id
  }

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-peer-public-route-table"
    }
  )
}

# Associate the peer route table

resource "aws_route_table_association" "peer_public" {
  subnet_id = aws_subnet.peer_public.id

  route_table_id = aws_route_table.peer_public.id
}

# Create the VPC peering connection

resource "aws_vpc_peering_connection" "peer" {
  vpc_id      = aws_vpc.main.id
  peer_vpc_id = aws_vpc.peer.id

  auto_accept = true

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-vpc-peering"
    }
  )
}

# Create the route to the peer VPC

resource "aws_route" "main_to_peer" {
  route_table_id = aws_route_table.private.id

  destination_cidr_block = aws_vpc.peer.cidr_block

  vpc_peering_connection_id = aws_vpc_peering_connection.peer.id
}

# Create the route back to the main VPC

resource "aws_route" "peer_to_main" {
  route_table_id = aws_route_table.peer_public.id

  destination_cidr_block = aws_vpc.main.cidr_block

  vpc_peering_connection_id = aws_vpc_peering_connection.peer.id
}